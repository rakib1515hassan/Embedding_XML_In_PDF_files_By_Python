import fitz  # PyMuPDF
import os

class PDFWithEmbeddedXML:
    def __init__(self, pdf_path, xml_path):
        self.pdf_path = pdf_path
        self.xml_path = xml_path
        self.temp_pdf_path = "temp_output.pdf"

    def read_xml_file(self):
        with open(self.xml_path, 'r', encoding='utf-8') as xml_file:
            xml_data = xml_file.read()
        return xml_data

    def create_pdf(self):
        doc = fitz.open()  # Create a new PDF document
        page = doc.new_page()  # Add a new page to the document
        page.insert_text((100, 750), "Simple Invoice PDF with Embedded XML")
        page.insert_text((100, 730), "Invoice Number: LTH-24-267")
        page.insert_text((100, 710), "Issue Date: 2024-10-03")
        page.insert_text((100, 690), "Seller: L&T Hydrocarbon Saudi Company")
        page.insert_text((100, 670), "Buyer: Larsen Toubro Arabia LLC")
        doc.save(self.temp_pdf_path)

    def embed_xml_in_pdf(self):
        self.create_pdf()
        
        xml_data = self.read_xml_file().encode('utf-8')
        
        # Open the temporary PDF
        with fitz.open(self.temp_pdf_path) as doc:
            # Embed the XML file as an attachment using the correct method
            doc.embfile_add("info.xml", xml_data)
            # Save the final PDF with the embedded XML
            doc.save(self.pdf_path)

        # Ensure the temp file is removed after closing
        os.remove(self.temp_pdf_path)

if __name__ == '__main__':
    pdf_path = "invoice_with_embedded_xml.pdf"
    xml_path = "Data/info.xml"  

    pdf_with_xml = PDFWithEmbeddedXML(pdf_path, xml_path)
    pdf_with_xml.embed_xml_in_pdf()
