from fpdf import FPDF
from xml.etree import ElementTree as ET

def xml_to_pdf(xml_content: bytes, output_pdf: str):
    # Parse the XML content from a byte string
    # Into an ElementTree object
    root = ET.fromstring(xml_content)
    pdf = FPDF()

    # Add a new page to the PDF and set the font
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Iterate through all elements in the XML tree
    for element in root.iter():
        text = (element.text or '').strip()
        if text:
            # Replace thin space with a regular space
            text = text.replace('\u2009', ' ') 
            # Encode the text to 'latin1'
            # then decode back to a string
            pdf.multi_cell(0, 10, text.encode('latin1', 'ignore').decode('latin1'))
    pdf.output(output_pdf)

