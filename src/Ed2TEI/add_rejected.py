# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:55:36 2024

@author: DelphDem
"""

import xml.etree.ElementTree as ET
import re
import argparse

# Register the XML namespace
ET.register_namespace('', "http://www.tei-c.org/ns/1.0")
ET.register_namespace('xml', "http://www.w3.org/XML/1998/namespace")

# Function to parse the rejected readings and return <choice> element
def parse_rejected_text(rejected_text):
    # This regex captures the corrected form (lemma) and the rejected reading
    match = re.match(r'\(([^)]+)\)\s*(.+)', rejected_text)
    if match:
        corr_text, sic_text = match.groups()
        corr_text = corr_text.strip()
        sic_text = sic_text.strip()

        # Create the <choice> element
        choice_element = ET.Element('choice')
        sic_element = ET.SubElement(choice_element, 'sic')
        sic_element.text = sic_text
        corr_element = ET.SubElement(choice_element, 'corr', {'resp': '#EDT'})
        corr_element.text = corr_text

        return choice_element, corr_text
    else:
        print(f"Rejected reading format error: '{rejected_text}'")
        return None, None

# Function to insert rejected readings into the TEI file
def add_rejected(tei_file, rejected_info, output_file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(tei_file, parser=parser)
    root = tree.getroot()
    ns = {'tei': "http://www.tei-c.org/ns/1.0", 'xml': "http://www.w3.org/XML/1998/namespace"}

    for line_id, rejected_text in rejected_info.items():
        tei_line_id = f"L{line_id}"
        l_element = root.find(f'.//tei:l[@xml:id="{tei_line_id}"]', ns)

        if l_element is not None:
            # Prepare the original text of the line
            line_text = ''.join(l_element.itertext())

            # Split multiple rejected readings by semicolon and process each
            rejected_parts = [part.strip() for part in rejected_text.split(';') if part.strip()]
            new_content = []
            last_pos = 0

            for rejected_part in rejected_parts:
                choice_element, corr_text = parse_rejected_text(rejected_part)

                if choice_element is not None:
                    # Find the position of the corrected text (lemma) in the line text
                    lemma_pos = line_text.find(corr_text, last_pos)

                    if lemma_pos != -1:
                        # Append the text before the lemma and the <choice> element
                        before_lemma = line_text[last_pos:lemma_pos]
                        new_content.append(before_lemma)
                        new_content.append(choice_element)

                        # Update the position after the lemma
                        last_pos = lemma_pos + len(corr_text)
                    else:
                        print(f"Corrected text '{corr_text}' not found in line {tei_line_id}.")
            
            # Append the remaining text after the last lemma
            remaining_text = line_text[last_pos:]
            new_content.append(remaining_text)

            # Clear the original <l> element and reconstruct it with new content
            l_element.clear()
            l_element.set('{http://www.w3.org/XML/1998/namespace}id', tei_line_id)

            # Set the first text part if it exists
            if isinstance(new_content[0], str):
                l_element.text = new_content[0]
                new_content = new_content[1:]

            # Append the rest of the <choice> elements and text
            for part in new_content:
                if isinstance(part, str):
                    if len(l_element) > 0:
                        l_element[-1].tail = part
                    else:
                        l_element.text = part
                else:
                    l_element.append(part)

            print(f"Added <choice> to line ID {tei_line_id}")
        else:
            print(f"Line ID {tei_line_id} not found in the TEI file. Skipping rejected entry...")

    # Save the updated TEI file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Function to read the rejected readings from the file
def read_rejected_from_file(file_path):
    rejected_readings = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(\d+)\s+(.*)$', line.strip())
                if match:
                    line_id, text = match.groups()
                    rejected_readings[line_id] = text
    except FileNotFoundError:
        print(f"Rejected readings file not found: {file_path}")
    return rejected_readings

def main():
    """Main function to handle CLI arguments and execute the add_rejected function."""
    parser = argparse.ArgumentParser(description="Add rejected readings to a TEI file.")
    parser.add_argument("--tei_file", required=True, help="The path to the TEI XML file to modify.")
    parser.add_argument("--rejected_file", required=True, help="The path to the text file containing rejected readings.")
    parser.add_argument("--output_file", required=True, help="The path to save the modified TEI file.")
    
    args = parser.parse_args()

    # Read the rejected readings from the provided text file
    rejected_info = read_rejected_from_file(args.rejected_file)

    # Add rejected readings to the TEI file
    add_rejected(args.tei_file, rejected_info, args.output_file)


if __name__ == "__main__":
    main()