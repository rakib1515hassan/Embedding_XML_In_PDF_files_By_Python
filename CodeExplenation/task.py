import fitz  # PyMuPDF
import os

# PDF ফাইলের সাথে এম্বেড করা XML সহ একটি ক্লাস
class PDFWithEmbeddedXML:

    def __init__(self, pdf_path, xml_path):
        # পিডিএফ এবং XML ফাইলের পাথ সেট করা
        self.pdf_path = pdf_path
        self.xml_path = xml_path
        self.temp_pdf_path = "temp_output.pdf"  # অস্থায়ী পিডিএফ ফাইলের পাথ


    # XML ফাইলটি পড়ার জন্য ফাংশন
    def read_xml_file(self):
        with open(self.xml_path, 'r', encoding='utf-8') as xml_file:
            xml_data = xml_file.read()  # XML ডেটা পড়া
        return xml_data
    
    

    # পিডিএফ ফাইল তৈরি করার জন্য ফাংশন
    def create_pdf(self):
        doc = fitz.open()     #? Create a new PDF document
        page = doc.new_page() #? Add a new page to the document

        # পৃষ্ঠায় কিছু টেক্সট যোগ করা
        page.insert_text((100, 750), "Simple Invoice PDF with Embedded XML")
        page.insert_text((100, 730), "Invoice Number: LTH-24-267")
        page.insert_text((100, 710), "Issue Date: 2024-10-03")
        page.insert_text((100, 690), "Seller: L&T Hydrocarbon Saudi Company")
        page.insert_text((100, 670), "Buyer: Larsen Toubro Arabia LLC")

        
        doc.save(self.temp_pdf_path)  # অস্থায়ী পিডিএফ ফাইলটি সংরক্ষণ করা



    # পিডিএফ ফাইলে XML এম্বেড করার জন্য ফাংশন
    def embed_xml_in_pdf(self):
        # প্রথমে পিডিএফ তৈরি করা
        self.create_pdf()
        
        # XML ফাইলের ডেটা পড়া
        xml_data = self.read_xml_file().encode('utf-8')  # XML ডেটাকে বাইনারি আকারে রূপান্তর করা
        
        # অস্থায়ী পিডিএফ ফাইল খোলা
        with fitz.open(self.temp_pdf_path) as doc:
            # XML ফাইলটি পিডিএফে এম্বেড করা
            doc.embfile_add("info.xml", xml_data)
            # ফাইনাল পিডিএফটি XML সহ সংরক্ষণ করা
            doc.save(self.pdf_path)

        # অস্থায়ী ফাইলটি ডিলিট করা
        os.remove(self.temp_pdf_path)



# প্রোগ্রাম রান করা হলে, নিচের অংশে কোডটি কার্যকর হবে
if __name__ == '__main__':
    pdf_path = "invoice_with_embedded_xml.pdf"  # আউটপুট পিডিএফ ফাইলের পাথ
    xml_path = "Data/info.xml"  # XML ফাইলের পাথ

    # PDFWithEmbeddedXML ক্লাসের একটি উদাহরণ তৈরি করা
    pdf_with_xml = PDFWithEmbeddedXML(pdf_path, xml_path)
    # XML সহ পিডিএফ এম্বেড করা
    pdf_with_xml.embed_xml_in_pdf()





