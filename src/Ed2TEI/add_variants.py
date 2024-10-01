# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:55:25 2024

@author: DelphDem
"""

import xml.etree.ElementTree as ET
import re
import argparse

# Register the XML namespace
ET.register_namespace('', "http://www.tei-c.org/ns/1.0")
ET.register_namespace('xml', "http://www.w3.org/XML/1998/namespace")

def parse_variant_text(variant_text):
    # This regex captures the lemma, multiple readings, and their respective witnesses
    parts = re.findall(r'\(([^)]+)\)\s*([^\[\(\]]+)(?:\s*\[(.*?)\])?', variant_text)
    app_elements = {}

    for lemma, readings, witnesses in parts:
        lemma = lemma.strip()
        readings = [r.strip() for r in re.split(r'\s(?=\[|$)', readings) if r.strip()]

        # Split multiple witnesses separated by commas (e.g., [C,P]) into individual witness IDs
        witnesses_list = witnesses.split(',') if witnesses else []

        # Create the <app> element and lemma element
        if lemma not in app_elements:
            app_element = ET.Element('app', {'type': 'variant'})
            lem_element = ET.SubElement(app_element, 'lem')
            lem_element.text = lemma
            app_elements[lemma] = app_element

        # Handle multiple readings and their witnesses
        for i, reading in enumerate(readings):
            if reading:  # Ignore empty readings
                # Format multiple witnesses as a space-separated list
                wit = " ".join(f"#{w.strip()}" for w in witnesses_list) if witnesses_list else "#unknown"
                rdg_element = ET.SubElement(app_elements[lemma], 'rdg', {'wit': wit})
                rdg_element.text = reading.strip()  # Ensure there is no trailing space

    return app_elements

def add_variants(tei_file, variants_info, output_file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(tei_file, parser=parser)
    root = tree.getroot()
    ns = {'tei': "http://www.tei-c.org/ns/1.0", 'xml': "http://www.w3.org/XML/1998/namespace"}

    for line_id, variant_text in variants_info.items():
        tei_line_id = f"L{line_id}"
        l_element = root.find(f'.//tei:l[@xml:id="{tei_line_id}"]', ns)
        
        if l_element is not None:
            app_elements = parse_variant_text(variant_text)
            
            # Prepare the original text of the line
            line_text = ''.join(l_element.itertext())
            
            # Sort lemmas by order of appearance in the line text
            lemmas = sorted(app_elements.keys(), key=lambda x: line_text.find(x))
            
            # Reset the <l> element
            l_element.clear()
            l_element.set('{http://www.w3.org/XML/1998/namespace}id', tei_line_id)
            
            # Initialize position to track text
            pos = 0

            for lemma in lemmas:
                # Find where the lemma is in the line text
                lemma_pos = line_text.find(lemma, pos)
                if lemma_pos == -1:
                    print(f"Lemma '{lemma}' not found in line {tei_line_id}.")
                    continue
                
                # Add the text before the lemma
                before_lemma = line_text[pos:lemma_pos]
                if before_lemma:
                    if not l_element.text:
                        l_element.text = before_lemma
                    else:
                        last_elem = l_element[-1] if len(l_element) > 0 else None
                        if last_elem is not None:
                            last_elem.tail = before_lemma
                        else:
                            l_element.text += before_lemma
                
                # Insert the <app> element for the lemma
                l_element.append(app_elements[lemma])
                
                # Move the position past the current lemma
                pos = lemma_pos + len(lemma)
            
            # Add the remaining text after the last lemma
            if pos < len(line_text):
                if len(l_element):
                    l_element[-1].tail = line_text[pos:]
                else:
                    l_element.text = line_text[pos:]
                    
            print(f"Added variant <app> to line ID {tei_line_id}")
        else:
            print(f"Line ID {tei_line_id} not found in the TEI file. Skipping variant entry...")

    # Save the updated TEI file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def read_variants_from_file(file_path):
    variants = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(\d+)\s+(.*)$', line.strip())
                if match:
                    line_id, text = match.groups()
                    if line_id not in variants:
                        variants[line_id] = text
                    else:
                        variants[line_id] += f" {text}"
    except FileNotFoundError:
        print(f"Variants file not found: {file_path}")
    return variants

def main():
    parser = argparse.ArgumentParser(description="Add variant readings to a TEI file.")
    parser.add_argument("--tei_file", required=True, help="The path to the TEI XML file to modify.")
    parser.add_argument("--variants_file", required=True, help="The path to the text file containing variant readings.")
    parser.add_argument("--output_file", required=True, help="The path to save the modified TEI file.")
    
    args = parser.parse_args()

    # Read the variants from the provided text file
    variants_info = read_variants_from_file(args.variants_file)

    # Add variants to the TEI file
    add_variants(args.tei_file, variants_info, args.output_file)


if __name__ == "__main__":
    main()
