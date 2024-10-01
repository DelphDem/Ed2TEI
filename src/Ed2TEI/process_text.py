# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:55:04 2024

@author: DelphDem
"""

import argparse
import re

def arabic_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for (arabic, roman) in roman_numerals:
        while number >= arabic:
            result += roman
            number -= arabic
    return result

def create_tei(input_file, output_file, is_verse=True, number_stanzas_paragraphs=False, use_roman_numerals=False, number_lines_every=4, reset_counts_on_page_break=False):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        line_count = 0
        stanza_count = 0
        paragraph_count = 0
        in_paragraph = False
        in_stanza = False
        page_line_count = 0

        outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        outfile.write('<TEI xmlns="http://www.tei-c.org/ns/1.0">\n')
        outfile.write('<teiHeader>\n')
        outfile.write('  <fileDesc>\n')
        outfile.write('    <titleStmt>\n')
        outfile.write('      <title></title>\n')
        outfile.write('    </titleStmt>\n')
        outfile.write('    <publicationStmt><p></p></publicationStmt>\n')
        outfile.write('    <sourceDesc><p></p></sourceDesc>\n')
        outfile.write('  </fileDesc>\n')
        outfile.write('</teiHeader>\n')
        outfile.write('  <text>\n')
        outfile.write('    <body>\n')
        outfile.write('    <div>\n')

        for line in lines:
            stripped_line = line.strip()
            line = re.sub(r'^\d+\s*', '', line)

            if stripped_line.startswith('<p'):
                if '>' in stripped_line:
                    page_number, remaining_text = stripped_line[2:].split('>', 1)
                else:
                    page_number = stripped_line[2:]
                    remaining_text = ""

                outfile.write(f'    <pb ed="base" n="{page_number.strip()}"/>\n')
                if reset_counts_on_page_break:
                    paragraph_count = 0  # Reset the paragraph counter at each page break
                    stanza_count = 0     # Reset the stanza counter at each page break
                    page_line_count = 0  # Reset the line count for n="" at each page break

                if remaining_text.strip():
                    stripped_line = remaining_text.strip()
                else:
                    continue

            if '[f.' in stripped_line:
                parts = re.split(r'(\[f\.\s*\d+[a-zA-Z]?\])', stripped_line)
                folio_inserted = False
                for part in parts:
                    match = re.search(r'\[f\.\s*(\d+[a-zA-Z]?)\]', part)
                    if match:
                        folio_number = match.group(1)
                        if folio_inserted:
                            outfile.write(f'    <pb ed="folio" n="{folio_number.strip()}"/>')
                        else:
                            folio_inserted = True
                            stripped_line = stripped_line.replace(part, f'<pb ed="folio" n="{folio_number.strip()}"/>', 1)
                    
            if not stripped_line:
                if in_paragraph:
                    outfile.write('    </p>\n')
                    in_paragraph = False
                if in_stanza:
                    outfile.write('    </lg>\n')
                    in_stanza = False
                continue

            # Handle stanza or paragraph opening
            if is_verse:
                if not in_stanza:
                    stanza_count += 1
                    stanza_number = arabic_to_roman(stanza_count) if use_roman_numerals else stanza_count
                    if number_stanzas_paragraphs:
                        outfile.write(f'    <lg n="{stanza_number}">\n')
                    else:
                        outfile.write('    <lg>\n')
                    in_stanza = True
            else:
                if not in_paragraph:
                    paragraph_count += 1
                    paragraph_number = arabic_to_roman(paragraph_count) if use_roman_numerals else paragraph_count
                    if number_stanzas_paragraphs:
                        outfile.write(f'    <p n="{paragraph_number}">\n')
                    else:
                        outfile.write('    <p>\n')
                    in_paragraph = True

            # Increment the line_count for line IDs
            line_count += 1
            page_line_count += 1  # Increment the line count for n=""

            if stripped_line[0].isdigit():
                line_content = stripped_line.split(maxsplit=1)[1]
            else:
                line_content = stripped_line

            line_id = f"L{line_count}"  # Retain the line count for line IDs
            if page_line_count % number_lines_every == 0:
                outfile.write(f'      <l n="{page_line_count}" xml:id="{line_id}">{line_content}</l>\n')
            else:
                outfile.write(f'      <l xml:id="{line_id}">{line_content}</l>\n')

        if in_paragraph:
            outfile.write('    </p>\n')
        if in_stanza:
            outfile.write('    </lg>\n')

        outfile.write('    </div>\n')
        outfile.write('    </body>\n')
        outfile.write('  </text>\n')
        outfile.write('</TEI>\n')

    # Print success message
    print(f"Successfully created TEI file: {output_file}")
    
def main():
    parser = argparse.ArgumentParser(description="Process text into TEI XML format.")
    parser.add_argument('input_file', help='Path to the input text file.')
    parser.add_argument('output_file', help='Path to the output TEI XML file.')
    parser.add_argument('--is_verse', action='store_true', help='Process as verse.')
    parser.add_argument('--number_stanzas_paragraphs', action='store_true', help='Number stanzas or paragraphs.')
    parser.add_argument('--use_roman_numerals', action='store_true', help='Use Roman numerals for numbering.')
    parser.add_argument('--number_lines_every', type=int, default=4, help='Number lines every N lines.')
    parser.add_argument('--reset_counts_on_page_break', action='store_true', help='Reset line and paragraph counts at every page break.')
    
    args = parser.parse_args()
    create_tei(
        args.input_file,
        args.output_file,
        is_verse=args.is_verse,
        number_stanzas_paragraphs=args.number_stanzas_paragraphs,
        use_roman_numerals=args.use_roman_numerals,
        number_lines_every=args.number_lines_every,
        reset_counts_on_page_break=args.reset_counts_on_page_break
    )

if __name__ == "__main__":
    main()
