from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, create_string_object, DecodedStreamObject, DictionaryObject

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
        c = canvas.Canvas(self.temp_pdf_path, pagesize=A4)
        c.drawString(100, 750, "Simple Invoice PDF with Embedded XML")
        c.drawString(100, 730, "Invoice Number: LTH-24-267")
        c.drawString(100, 710, "Issue Date: 2024-10-03")
        c.drawString(100, 690, "Seller: L&T Hydrocarbon Saudi Company")
        c.drawString(100, 670, "Buyer: Larsen Toubro Arabia LLC")
        c.showPage()
        c.save()

    def embed_xml_in_pdf(self):
        self.create_pdf()
        
        xml_data = self.read_xml_file().encode('utf-8')
        
        reader = PdfReader(self.temp_pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)
        
        file_entry = DecodedStreamObject()
        file_entry.set_data(xml_data)
        file_entry.update({
            NameObject("/Type"): NameObject("/EmbeddedFile"),
            NameObject("/Subtype"): NameObject("/text#2Fxml")
        })

        file_spec = DictionaryObject()
        file_spec.update({
            NameObject("/Type"): NameObject("/Filespec"),
            NameObject("/F"): create_string_object("info.xml"),
            NameObject("/EF"): DictionaryObject({
                NameObject("/F"): file_entry
            })
        })

        writer.add_attachment("info.xml", xml_data)

        with open(self.pdf_path, "wb") as f_out:
            writer.write(f_out)

        os.remove(self.temp_pdf_path)

if __name__ == '__main__':
    pdf_path = "invoice_with_embedded_xml.pdf"
    xml_path = "Data/info.xml"  

    pdf_with_xml = PDFWithEmbeddedXML(pdf_path, xml_path)
    pdf_with_xml.embed_xml_in_pdf()
