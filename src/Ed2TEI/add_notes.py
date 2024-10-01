# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:55:47 2024

@author: DelphDem
"""
import xml.etree.ElementTree as ET
import re
import argparse

# Register the XML namespace
ET.register_namespace('', "http://www.tei-c.org/ns/1.0")
ET.register_namespace('xml', "http://www.w3.org/XML/1998/namespace")

# Function to parse the note text
def parse_note_text(note_text):
    # This regex captures the bracketed location text and the note content
    match = re.match(r'\(([^)]+)\)\s*(.+)', note_text)
    if match:
        location_text, note_content = match.groups()
        location_text = location_text.strip()
        note_content = note_content.strip()
        return location_text, note_content
    else:
        print(f"Note format error: '{note_text}'")
        return None, None

# Function to insert notes into the TEI file
def add_notes(tei_file, notes_info, output_file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(tei_file, parser=parser)
    root = tree.getroot()
    ns = {'tei': "http://www.tei-c.org/ns/1.0", 'xml': "http://www.w3.org/XML/1998/namespace"}

    # Initialize note counter
    note_counter = 1

    for line_id, note_text in notes_info.items():
        tei_line_id = f"L{line_id}"
        l_element = root.find(f'.//tei:l[@xml:id="{tei_line_id}"]', ns)

        if l_element is not None:
            # Prepare the original text of the line
            line_text = ''.join(l_element.itertext())

            # Parse the note text to get the location and content
            location_text, note_content = parse_note_text(note_text)

            if location_text and note_content:
                # Find the position of the location text in the line text
                location_pos = line_text.find(location_text)

                if location_pos != -1:
                    # Create the <note> element
                    note_element = ET.Element('note', {'resp': '#EDT', 'n': str(note_counter)})
                    note_element.text = note_content

                    # Increment the note counter
                    note_counter += 1

                    # Insert the note at the correct position in the line
                    before_location = line_text[:location_pos + len(location_text)]
                    after_location = line_text[location_pos + len(location_text):]

                    # Clear the original <l> element and reconstruct it
                    l_element.clear()
                    l_element.set('{http://www.w3.org/XML/1998/namespace}id', tei_line_id)

                    l_element.text = before_location
                    l_element.append(note_element)
                    note_element.tail = after_location

                    print(f"Added <note> to line ID {tei_line_id}")
                else:
                    print(f"Location text '{location_text}' not found in line {tei_line_id}.")
            else:
                print(f"Skipping malformed note in line {line_id}: '{note_text}'")
        else:
            print(f"Line ID {tei_line_id} not found in the TEI file. Skipping note entry...")

    # Save the updated TEI file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Function to read the notes from the file
def read_notes_from_file(file_path):
    notes = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.match(r'^(\d+)\s+(.*)$', line.strip())
                if match:
                    line_id, text = match.groups()
                    notes[line_id] = text
    except FileNotFoundError:
        print(f"Notes file not found: {file_path}")
    return notes

def main():
    """Main function to handle CLI arguments and execute the add_notes function."""
    parser = argparse.ArgumentParser(description="Add notes to a TEI file.")
    parser.add_argument("--tei_file", required=True, help="The path to the TEI XML file to modify.")
    parser.add_argument("--notes_file", required=True, help="The path to the text file containing notes.")
    parser.add_argument("--output_file", required=True, help="The path to save the modified TEI file.")

    args = parser.parse_args()

    # Read the notes from the provided text file
    notes_info = read_notes_from_file(args.notes_file)

    # Add notes to the TEI file
    add_notes(args.tei_file, notes_info, args.output_file)


if __name__ == "__main__":
    main()