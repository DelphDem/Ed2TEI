---
title: 'Ed2TEI: An Automated Tool for Encoding texts and Critical Apparatus into TEI XML'
tags:
  - Python
  - TEI (Text Encoding Initiative)
  - Critical Editions
  - Digital Humanities
  - Text Encoding
  - XML
  - Scholarly Editing
  - Corpus Linguistics
authors:
  - name: Delphine Demelas
    orcid: 0000-0002-2414-4581
    equal-contrib: true
    affiliation: "Aberystwyth University (UK)"
date: 02 October 2024
bibliography: paper.bib
---

# Summary

The `Ed2TEI` package was developed to automate the process of [TEI XML encoding](https://tei-c.org/) for critical editions and variant readings, making it accessible to editors and scholars who may not have extensive experience with XML. By allowing users to work directly with structured plain text files, the tool removes the steep learning curve associated with XML-based markup. These .txt files can easily be produced or adapted from commonly used formats for paper editions, such as .doc or .pdf, facilitating the transition from print to digital editions.

Key features of `Ed2TEI` include automated tagging for variant readings, rejected readings, and editorial notes, as well as flexible handling of different types of textual elements, such as verse and prose. The package can handle complex scenarios that are typically time-consuming to encode in TEI XML P5, like multiple  variants for one lemmata linked to multiple witnesses. As a result, `Ed2TEI` significantly reduces the manual effort required to produce a TEI-compliant document, while maintaining the precision needed for scholarly editions.

The package is particularly suited for editors and researchers who need to work with large corpora or individual texts, making it a versatile tool for a wide range of textual projects. Initially designed by Delphine Demelas to speed up TEI XML marking for the [Anglo-Norman Dictionary Online Textbase](https://www.anglo-norman.net/textbase-browse/) in 2024, the tool has been successfully used to encode a number of new editions and published editions in TEI XML format. Its flexibility and ease of use make it a valuable resource for anyone looking to build a TEI corpus or digitize complex critical editions.

# Statement of need

The creation and modification of critical editions in digital formats, particularly TEI (Text Encoding Initiative) XML, are vital components of digital humanities scholarship [@fischer_representing_2020, @burghart_creating_2017, @alcaraz-martinez_tei_2016]. TEI-compliant editions provide a standardized and machine-readable format that allows for long-term preservation, interoperability, and advanced computational analysis of textual data. For many years, the Text Encoding Initiative has strived to develop a global standard for the digital encoding of textual information within the humanities [@ide_tei_1995]. Their guidelines offer a consistent framework for representing physical characteristics of sources, textual transcriptions, and critical apparatuses [@tei_2024]. As a result, the Text Encoding Initiative’s Extensible Markup Language format (commonly referred to as TEI XML) has emerged as the primary standard in the digital humanities, owing to its extensive and well-documented set of elements for describing diverse textual features in various contexts.

Despite these benefits, many editors and textual scholars remain hesitant to adopt TEI due to two primary obstacles: lack of technical expertise and the labor-intensive nature of encoding complex textual features [@romary_questions_2008].

 1. **Lack of Technical Knowledge**: For many scholars, TEI can appear daunting and complex, requiring familiarity with XML syntax, TEI guidelines, and appropriate encoding practices. This learning curve often discourages editors from adopting TEI for their own projects, resulting in limited dissemination and digital availability of critical editions.
2. **Time-Consuming Encoding**: The process of tagging each variant, rejected reading, and editorial note in a critical apparatus is extremely time-consuming and prone to errors. Traditional manual encoding demands meticulous attention to detail, making it difficult to produce consistent and comprehensive editions without significant investments in time and effort.

`Ed2TEI` is designed specifically to address these issues and encourage wider adoption of TEI encoding among editors and textual scholars. This package provides a user-friendly, automated solution that reduces the amount of manual work required to produce a TEI-compliant edition. By offering functions that can batch-process variant readings, rejected readings, and editorial notes based on structured input files, Ed2TEI minimizes the need for extensive XML expertise while ensuring the accuracy and consistency of the encoded content.

`Ed2TEI` thus seeks to support users who wish to publish their work in TEI by providing a tool that is easy to use, yet powerful enough to handle complex critical apparatus features. It enables editors to focus on the scholarly aspects of their work rather than getting bogged down in technical details. Ultimately, this package aims to make TEI more accessible and less time-consuming, bridging the gap between traditional textual scholarship and modern digital editions.

The package is useful for:

* Editors wanting to publish critical editions in TEI without the steep learning curve.
* Large-scale digital projects aiming to build a corpus of TEI-encoded texts based on traditional paper editions.
* Any project needing to integrate complex variant readings, rejected readings, or editorial notes into TEI without manual tagging.
    
By lowering the barrier to entry for TEI encoding and streamlining the encoding process, `Ed2TEI` allows a broader range of scholars to contribute to the digital scholarly ecosystem and to publish high-quality, TEI-compliant critical editions without compromising on editorial precision or completeness.

# Features
The `Ed2TEI` package offers several key features designed to streamline the conversion of critical editions into TEI XML P5 format:

1. **TEI XML Creation for Verse and Prose Texts:**
    The create_tei function allows users to automatically generate a TEI XML file from a structured .txt file, whether it contains verse or prose formatting. Users can specify options for handling different numbering styles (Arabic or Roman), page breaks and folio breaks, resetting counts at page breaks, and more. This feature is ideal for converting large plain text editions into TEI XML without manually encoding every line, enabling users to focus on the textual content itself.

2. **Automated Variant Insertion:**
    Efficiently insert complex variant readings into your TEI XML file by processing structured plain text files. This feature enables scholars to maintain detailed textual variants without manually coding each XML elements, saving significant time and effort.

3. **Rejected Readings Tagging:**
    Automatically tags rejected readings using `<choice>`, `<sic>`, and `<corr>` elements, allowing editors to clearly indicate corrections or alternate readings within the text. This feature is ideal for tracking editorial decisions and preserving transparency in the text’s transmission history.

4. **Editorial Notes Tagging:**
    Supports the insertion of editorial notes using the `<note>` element based on specific text locations. Users can specify where each note should appear using a straightforward plain-text notation, making it simple to add commentary or context for readers.

5. **Flexible File Formats:**
    The package can handle structured text files with customizable options for critical apparatus tagging. It offers support for a variety of textual structures commonly used in critical editions, such as verse, prose, and mixed formats, providing flexibility and compatibility with a wide range of scholarly texts.

These features are designed to make TEI XML creation more accessible, especially for users who are new to TEI encoding or those working with large-scale corpora. `Ed2TEI` provides a solution for quickly generating high-quality TEI documents from plain text sources, minimizing the effort required for detailed critical apparatus encoding.

# Related Frameworks

The landscape of TEI (Text Encoding Initiative) tools includes several established platforms designed to facilitate the encoding, management, and publication of TEI-based scholarly texts. Among these tools, TEI Publisher is one of the most widely known solutions. It offers a robust environment for displaying, navigating, and querying TEI documents, making it a popular choice for digital editions. 

**TEI Publisher** [@teipublisher_2016] is particularly useful for creating interactive interfaces that allow for rich exploration of texts, including features like faceted search, annotations, and user comments. It is built on eXist-db, a native XML database, which provides strong backend support for complex querying and data retrieval.

The **TEIGarage** [@teigarage_2024] tool provide o the TEI website is used for converting documents between different formats, including TEI and Word. While useful for format conversion, it doesn’t provide support for the complexities of critical editions. TEIGarage does not handle complex tasks like tagging variants, rejected readings, and editorial notes with minimal user input​.

Other tools include [**oXygen XML Editor**](https://www.oxygenxml.com/), a comprehensive XML editing environment that provides support for TEI schema validation, transformation, and visualization. oXygen’s strengths lie in its detailed, real-time TEI markup assistance and XSLT processing, which are valuable for advanced users creating complex TEI documents. It also integrates well with other TEI tools and offers features like side-by-side comparisons and real-time previews of encoded texts.

[**TEI Boilerplate**](http://teiboilerplate.org/) is an additional tool focused on specific aspects of TEI document handling. TEI Boilerplate is primarily a front-end solution for rendering TEI documents in web browsers using CSS and JavaScript, providing a quick way to publish encoded texts without the need for server-side processing. Transpect, on the other hand, is a suite of tools for transforming TEI and other XML documents, making it useful for specific pipelines like conversion and print production.

**Ekdosis** [@alessi_ekdosis_2020] is a LuaLaTeX-based package designed for creating critical editions with complex textual structures. It allows users to generate TEI XML and parallel PDF outputs simultaneously, supporting features like variant apparatuses, parallel texts, and sophisticated critical notes. Developed for scholars who are comfortable with LaTeX, Ekdosis offers powerful tools for handling complex philological tasks, integrating typesetting and TEI encoding within the same framework. However, its reliance on LaTeX syntax and commands can be a significant barrier for users unfamiliar with the LaTeX ecosystem, limiting accessibility for those without specialized technical skills.

However, these tools, despite their powerful features, are not always well-suited for scholarly editors working on critical editions, focalizing mostly on visualisation. Editors who are unfamiliar with TEI may find the learning curve for tools like TEI Publisher and oXygen steep, and setting up a complete TEI database environment can be a complex and time-consuming process. For those working on large text corpora or wanting to quickly convert paper-based critical editions into digital TEI, the existing tools may require significant manual effort and technical expertise.

In contrast, `ED2TEI` offers a lightweight, user-friendly alternative focused specifically on the encoding texts and critical apparatuses, rejected readings, and editorial notes from structured text files. Unlike TEI Publisher, which is more oriented toward publishing and browsing TEI documents, `ED2TEI` is designed to streamline the encoding process itself, enabling scholars to produce well-formed TEI documents from simple text inputs. This approach lowers the barrier for scholars and editors with limited TEI experience or those who need to handle a large number of texts with minimal setup.

For projects where the goal is rapid encoding rather than visualization, `ED2TEI` provides an efficient solution. It is especially beneficial for editors managing large-scale projects with repetitive markup tasks, offering a straightforward path to transform structured textual input into TEI-compliant files with complex critical apparatus tagging. By addressing this niche, it fills a gap left by more comprehensive, but often more complex, TEI tools such as TEI Publisher and oXygen.

# Usage
##  Command-Line Usage

1. **Create TEI (`create_tei`):**

```
create_tei [options] --input_file [file_path] --output_file [output_file.xml] 
```
- Converts a plain text file into a formatted TEI XML document.
- Options include formatting for prose/verse, automatic numbering of lines, and custom tags.

2. **Add Variants (`add_variants`):**


```
add_variants --tei_file [tei_file.xml] --variants_file [variants.txt] --output_file [output_file.xml]
```
- Reads a structured text file of variants and automatically inserts <app>, <lem>, and <rdg> elements.

3. **Add Rejected Readings (`add_rejected`):**

```
add_rejected --tei_file [tei_file.xml] --rejected_file [rejected.txt] --output_file [output_file.xml]
```

- Handles rejected readings tagging using `<choice>`, `<sic>` and `<corr>` elements.

4. **Add Notes (`add_notes`):**

```
add_notes --tei_file [tei_file.xml] --notes_file [notes.txt] --output_file [output_file.xml]
```

- Tags notes into the TEI `<note>` structure based on location markers in the text file.

##  .Txt Files Fromat Requirements

To ensure the proper functioning of the package, the .txt files need to be structured in a specific format:

### 1. Text File

The .txt text file includes the text, the folio breaks and page breaks (where applicable). Each line break in the file will be consided as a a line using the `<l></l>` tags. Page breaks should be specified with `<p +volume number-page number>` (e.g.: `<p i-7`>, `<p. 8>`). Folio numbers will be indicated with square bracket: `[f.+folio number/r,v/column]` (e.g.: `[f.1ra]`). A blank line indicates a paragraph or stanza. See the [Txt_models folder](https://github.com/DelphDem/Ed2TEI/tree/main/Txt_models) for an example.

### 2. Variants File

The variants txt file should contain variant readings for each line in the TEI file. The format is:

```
line_number (lemma) variant [witness]
```

* **Line Number**: The line number in the TEI file, indicated with `xml:id="L+number"`, where the variant should be applied, without the 'L' prefix.
* **Lemma**: The main text found in the TEI file corresponding to the variant.It should be specified with round brackets.
* **Variants with Witnesses**: Each variant reading followed by its witness enclosed in square brackets; in case of several witness for one reading, witness should be separated by a comma. In case of multiple readings for one lemma, the lemma should be repated before each variant.

#### Example
For a unique variant:
```
6 (meisun) mansiun [C,P]
```
For multiple variants for the same lemma:

```
26 (Deu) om [C] (Deu) D. devine [D]
```

### 3. Rejected Readings File

The rejected readings file should specify corrections to be marked in the TEI file. The format is:

```
line_number (corrected_text) rejected_text
```

* **Line Number**: The line number in the TEI file, indicated with `xml:id="L+number"`, where the variant should be applied, without the 'L' prefix.
* **Corrected Text**: Text that should replace the rejected reading, enclosed in round brackets ().
* **Rejected Text**: The text that is currently in the òriginal text but should be marked as rejected.

The package provide examples for each type of file.

# Caveats

While the `Ed2TEI` package provides a more accessible way to encode complex critical editions in TEI, there are several caveats and limitations that potential users should be aware of:

- **Structured Text File Formatting:**
        One of the key aspects of Ed2TEI is the requirement to prepare structured text files in a specific format before using the tool. This initial setup process can take some time, especially for users new to the package or who are not familiar with the conventions of text encoding.
        Each type of element (e.g., variant readings, rejected readings, and notes) must follow distinct formatting rules, such as the use of parentheses to indicate lemmata, square brackets for witnesses, and specific line number references. These rules need to be followed precisely for the tool to parse and generate the expected TEI elements correctly.
        The formatting is less intimidating than coding every part of the TEI structure directly, but it can still be cumbersome for texts with intricate or overlapping annotations.

- **Learning Curve:**
        While `Ed2TEI` significantly simplifies the TEI encoding process compared to traditional manual encoding, there is still a learning curve. Users need to become familiar with the package's command-line interface, input formats, and options.
        Beginners without prior experience in Python or command-line tools may find the initial stages of using the package challenging. Familiarity with structured text formats and command-line basics will help, but some users might still require guidance through detailed examples and documentation.

- **Manual Text Preparation:**
        `Ed2TEI` relies on correctly prepared input text files to automate the encoding process. Thus, errors or inconsistencies in the input files can result in incorrect or incomplete TEI outputs.
        For instance, missing line references, incorrect witness tags, or mismatched variant annotations can cause parsing issues that may not always be obvious until the output file is reviewed.
        For larger projects, managing multiple structured text files (especially for different variants and rejected readings) can become complex, and the tool does not currently have built-in mechanisms to detect and flag inconsistencies in the input data.

- **Handling Complex or Overlapping Variants:**
        While the package handles a range of standard cases, complex or overlapping variants (e.g., multiple variants appearing in close proximity, or cases where a single reading corresponds to multiple witnesses across different locations) may require manual adjustments in the input file.
        `Ed2TEI`'s ability to insert variants relies on the precise matching of lemmata and text positions, which means that overlapping variants can occasionally result in inaccurate placements if not carefully structured beforehand.

- **Context-Sensitive Encoding:**
        The package cannot automatically infer contextual or interpretative aspects of the text, such as handling ambiguous variant readings or deciding how to tag more subjective editorial interventions. The input files must explicitly specify each case.
        As a result, `Ed2TEI` is best suited for well-prepared texts where all editorial decisions have already been made. Users looking for a tool to dynamically encode such contexts or handle edge cases on the fly may find the tool limited in this regard.

- **Performance with Large Files:**
        While `Ed2TEI` is optimized for a range of TEI encoding tasks, working with extremely large files or complex manuscripts with dense critical apparatus can affect performance. Users may notice slower processing times when dealing with thousands of lines or intricate variants, particularly if the input files are not optimized.
        For large-scale projects, it may be beneficial to split the input files into smaller chunks and process them sequentially, rather than attempting to encode an entire edition at once.

- **TEI Customization Limitations:**
        `Ed2TEI` currently supports a specific subset of TEI elements tailored to encoding critical apparatus features (e.g., `<app>`, `<rdg>`, `<sic>`, `<corr>`, and `<note>`). Users with more complex TEI customization needs, such as custom attribute values or specialized TEI modules, may need to manually adjust the generated TEI file or extend the package.

- **Suitability for Non-Critical Editions:**
        While `Ed2TEI` can be adapted for various scholarly texts, its primary design is focused on handling critical editions with apparatus features. Users working on non-critical texts or texts without variants may find some of the package’s functionalities redundant.
        For such cases, a simpler TEI editor or a lightweight encoding tool may be a better fit, unless there is a need for managing structured annotations or bulk processing of text files.

Despite these caveats, the overall time required to format the text files is significantly lower compared to directly encoding the XML file line-by-line using TEI elements. For users who are new to TEI or for those managing large corpora, the structured text input format offers a less daunting and more scalable approach to encoding complex critical apparatus features. By automating the repetitive parts of the TEI tagging process, `Ed2TEI` strikes a balance between flexibility and usability, making it a valuable tool for many scholars and editors.

# Availability

The Ed2TEI package is currently available exclusively on [GitHub](https://github.com/DelphDem/Ed2TEI) under the MIT license. It has not yet been published on the Python Package Index (PyPI), making it accessible for local use and custom development. Users can clone or download the repository directly from GitHub and follow the instructions in the README file to set up and run the package on their systems.

For access and installation details, visit the [GitHub repository](https://github.com/DelphDem/Ed2TEI).

# Future Work

While `Ed2TEI` already addresses many challenges related to TEI encoding for critical editions, there are several avenues for future development to further enhance its capabilities:

- **Expanded Support for Complex Tagging Options:**
        Future versions of Ed2TEI could incorporate support for additional TEI elements such as <abbr> for abbreviations and expansions, `<add>`, `<del>` and `<subst>` for additions, delations and substitutions in the source, and `<name>` for linking place and people names in texts with wikidata. These enhancements would allow users to encode a broader range of textual features without needing to modify the TEI files manually.

- **Integration with Other TEI Tools:**
        `Ed2TEI` could be enhanced by building bridges to other TEI tools, such as **TEI Publisher** or **TEIGarage**, to create a more comprehensive workflow for encoding, editing, and visualizing TEI files. This would provide users with an end-to-end solution that covers the entire publication pipeline, from initial encoding to digital presentation.

- **Text File Preparation Assistance:**
        One of the common challenges is preparing the structured text files in the precise format required by `Ed2TEI`. Future work could include a preprocessing module or a GUI tool that assists users in converting existing texts (e.g., Word documents, PDFs) into the appropriate structured txt format.
        Additionally, the package could include utilities to automate certain text formatting tasks (e.g., auto-numbering lines, identifying potential lemmata) to reduce the manual burden on users and prevent common formatting errors.

- **Automated Corpus Conversion:**
        Expanding the functionality to include bulk processing and conversion of multiple documents would be beneficial for projects building large TEI corpora. This could include options to batch-process entire directories of texts, along with the ability to validate the TEI output according to custom schemas.

- **Improving User Guidance and Documentation:**
        As part of the development roadmap, a focus on creating detailed tutorials and interactive documentation will be crucial to support new users in getting started. This could include video tutorials, an interactive setup wizard, or a repository of example text files for different use cases.

By addressing these potential enhancements, `Ed2TEI` can continue to grow into a comprehensive TEI encoding tool that meets the evolving needs of digital humanists and editors, helping them streamline their workflows and produce high-quality, interoperable digital editions.

These future improvements could not only broaden the package's applicability but also contribute to the ongoing adoption of TEI in the academic community, promoting the standardization and sustainability of digital scholarly editions.

# Conclusion

`Ed2TEI` offers a streamlined and efficient solution for encoding complex critical editions in TEI, addressing several pain points that scholars and editors face when publishing digital editions. One of the most significant contributions of this package is its ability to automate variant readings, rejected readings, and editorial note tagging using a structured text format, significantly reducing the time required for manual TEI tagging.

By simplifying the encoding process, `Ed2TEI` lowers the barrier for entry to TEI, making it accessible to those who may lack extensive XML expertise. This ease of use can encourage more editors and scholars to adopt TEI as a standard for their digital publications, thereby enhancing the quality, accessibility, and interoperability of scholarly editions.

Moreover, the tool’s design is the result of practical editorial experiences at the [*Anglo-Norman Dictionary*](https://anglo-norman.net/), demonstrating its suitability for both small-scale individual projects and large-scale corpus-building initiatives. `Ed2TEI` not only reduces the workload involved in tagging large quantities of text but also ensures consistency and accuracy in the TEI structure. This makes it a powerful resource for both novice users and experienced editors who are looking to expand their digital scholarly publishing efforts.

# Acknowledgements

This work was supported by the UKRI Arts and Humanities Research Council [(AHRC)](https://www.ukri.org/councils/ahrc).

# References
