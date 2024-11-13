from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from xml.etree.ElementTree import Element, SubElement, tostring
import io

class PDFWithEmbeddedXML:
    def __init__(self, path):
        self.path = path

    def create_xml_data(self, data):
        # Root element for the XML
        root = Element('Invoice')
        
        # Add invoice metadata
        SubElement(root, 'InvoiceNumber').text = data.get('invoice_number', 'N/A')
        SubElement(root, 'IssueDate').text = data.get('issue_date', 'N/A')
        
        # Add seller details
        seller = SubElement(root, 'Seller')
        SubElement(seller, 'Name').text = data['seller']['name']
        SubElement(seller, 'VATNumber').text = data['seller']['vat_number']
        
        # Add buyer details
        buyer = SubElement(root, 'Buyer')
        SubElement(buyer, 'Name').text = data['buyer']['name']
        SubElement(buyer, 'VATNumber').text = data['buyer']['vat_number']
        
        # Add line items
        items = SubElement(root, 'Items')
        for item in data['items']:
            item_element = SubElement(items, 'Item')
            SubElement(item_element, 'Description').text = item['description']
            SubElement(item_element, 'UnitPrice').text = str(item['unit_price'])
            SubElement(item_element, 'Quantity').text = str(item['quantity'])
            SubElement(item_element, 'Total').text = str(item['total'])
        
        # Generate XML string
        return tostring(root, encoding='utf-8').decode('utf-8')

    def embed_xml_in_pdf(self, data):
        c = canvas.Canvas(self.path, pagesize=A4)
        
        # Add PDF content
        c.drawString(100, 750, "Invoice PDF with Embedded XML")

        # Generate XML data and embed it as metadata
        xml_data = self.create_xml_data(data)
        
        # Set metadata with XML stream
        c._doc.info.producer = "PDF Generator with XML"
        c._doc.info.title = "Invoice with Embedded XML"
        c._doc.addAttachment('invoice_data.xml', xml_data.encode('utf-8'))

        # Finish PDF
        c.showPage()
        c.save()

# Data for PDF and XML generation
invoice_data = {
    'invoice_number': 'LTH-24-267',
    'issue_date': '2024-10-03',
    'seller': {
        'name': 'L&T Hydrocarbon Saudi Company',
        'vat_number': '300464605700003',
    },
    'buyer': {
        'name': 'Larsen Toubro Arabia LLC',
        'vat_number': '300600871100003',
    },
    'items': [
        {'description': 'Manpower Service to LTA for Sep24', 'unit_price': 1913917.33, 'quantity': 1, 'total': 1913917.33}
    ]
}

# Generate PDF with embedded XML
pdf_with_xml = PDFWithEmbeddedXML("invoice_with_xml.pdf")
pdf_with_xml.embed_xml_in_pdf(invoice_data)
