# Ed2TEI

`Ed2TEI` is a Python package designed to convert critical editions into structured TEI XML format following the TEI 5 Guidelines. The package allows users to create a TEI XML file from a txt file, and to automate the insertion of variant readings, rejected readings, and notes into a TEI file using structured txt files.

## Installation

You can install `Ed2TEI` using pip:

```
pip install Ed2TEI
```
## Features

- Create TEI Base File: Generate a basic TEI XML file from a plain text file.
- Automated Variant Insertion: Insert complex variant readings from several sources into your TEI XML file.
- Rejected Readings Tagging: Automatically tag rejected readings using `<choice>`, `<sic>`, and `<corr>` elements.
- Editorial Notes Tagging: Insert editorial notes using the `<note>` element based on text locations.
- Flexible File Formats: Supports various type of text with customizable options.


## Usage

The `Ed2TEI` package offers several command-line tools to handle different types of critical apparatus. Below is an overview of the main commands and their expected file formats. The model is based on the first paragraphs of Tony Hunt, *Sermons on Joshua*, vol1, ANTS Plain Texts Series 12-13, London, 1998. Some variants, notes, and rejected readings have been added to demonstrate the package's possibilities.

### 1. Creating a TEI Base File

The `create_tei` command is used to generate a base TEI file from a structured text file. This is typically the first step before adding variants, rejected readings, or notes.

#### Command
```bash
create_tei [options] --input_file <plain_text_file> --output_file <output_tei_file>
```
#### Options

* `--input_file` (required): Path to the txt file containing the main text to convert.
* `--output_file` (required): Path to the generated TEI XML file.
* `--is_verse` (optional): Process the text as verse (paragraph are tagged as stanza using the `<lg>` tag instead of `<p>`).
* `--number_lines_every` (optional): Number lines every N lines (default: number_lines_every=4).
* `--number_stanzas_paragraphs` (True/False): Stanzas or paragraphs are numbered (default=True).
* `--use_roman_numerals` (True/False): Use Roman numerals for numbering stanza or paragraph (default=False).
* `--reset_counts_on_page_break` (True/False): Reset line and paragraph counts at every page break (default=False).

### 2. Adding Variants

The `add_variants` command is used to insert variant readings into a TEI XML file.

#### Command

```bash
add_variants --tei_file <input_tei_file> --variants_file <variants_text_file> --output_file <output_tei_file>
````
#### Options

* `--tei_file` (required): Path to the input TEI XML file.
* `--variants_file` (required): Path to the text file containing variant readings.
* `--output_file` (required): Path to the output TEI XML file.

### 3. Adding Rejected Readings

The `add_rejected` command is used to insert rejected readings into a TEI XML file using the `<choice>`, `<sic>`, and `<corr>` tags. 

```bash
add_rejected --tei_file <input_tei_file> --variants_file <variants_text_file> --output_file <output_tei_file>
````
#### Options

* `--tei_file` (required): Path to the input TEI XML file.
* `--variants_file` (required): Path to the text file containing rejected readings.
* `--output_file` (required): Path to the output TEI XML file.

### 4. Inserting Editorial Notes

The `add_notes` command is used to add editorial notes to specified lines in a TEI XML file.

#### Options

* `--tei_file` (required): Path to the input TEI XML file.
* `--variants_file` (required): Path to the text file containing editorial readings.
* `--output_file` (required): Path to the output TEI XML file.

## File Format Requirements

To ensure the proper functioning of the package, the txt files need to be structured in a specific format:

### 1. Text File

The txt text file includes the text, the folio breaks and page breaks (where applicable). Each line break in the file will be consided as a a line using the `<l></l>` tags. Page breaks should be specified with `<p +volume number-page number>` (e.g.: `<p i-7`>, `<p. 8>`). Folio numbers will be indicated with square bracket: `[f.+folio number/r,v/column]` (e.g.: `[f.1ra]`). A blank line indicates a paragraph or stanza. See the Txt_models folder for an example.

### 2. Variants File

The variants txt file should contain variant readings for each line in the TEI file. The format is:

```scss

line number (lemma) variant [witness]

```

* **Line Number**: The line number in the TEI file, indicated with `xml:id="L+number"`, where the variant should be applied, without the 'L' prefix.
* **Lemma**: The main text found in the TEI file corresponding to the variant.It should be specified with round brackets.
* **Readings with Witnesses**: Each variant reading followed by its witness enclosed in square brackets; in case of several witness for one reading, witness should be separated by a comma. In case of multiple readings for one lemma, the lemma should be repated before each variant.

#### Example
For a unique variant:
```scss
6 (meisun) mansiun [C,P]
```
For multiple variants for the same lemma:

```scss
26 (Deu) om [C] (Deu) D. devine [D]
```

### 3. Rejected Readings File

The rejected readings file should specify corrections to be marked in the TEI file. The format is:

```scss
line_number (corrected_text) rejected_text
```

* **Line Number**: The line number in the TEI file, indicated with `xml:id="L+number"`, where the variant should be applied, without the 'L' prefix.
* **Corrected Text**: Text that should replace the rejected reading, enclosed in round brackets ().
* **Rejected Text**: The text that is currently in the òriginal text but should be marked as rejected.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
