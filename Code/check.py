import fitz  # PyMuPDF

def check_pdf_attachments(pdf_path):
    doc = fitz.open(pdf_path)

    # চেক করুন যে কোনও এম্বেডেড ফাইল আছে কিনা
    if doc.embfile_count() > 0:
        print("এম্বেডেড ফাইল পাওয়া গেছে:")  # "Embedded files found:"
        for i in range(doc.embfile_count()):
            # এম্বেডেড ফাইলের তথ্য একটি টিউপলে পাবেন
            embedded_file_info = doc.embfile_get(i)

            # টিউপলের প্রথম উপাদানটি হল ফাইলের নাম
            filename = str(embedded_file_info[0])  # Convert to string and lowercase

            print(f"ফাইল: {filename}")  # "File: filename"
            
            # চেক করুন যদি "info.xml" এম্বেডেড থাকে
            if filename.lower() == "info.xml".lower():
                print("XML ফাইল সফলভাবে সংযুক্ত হয়েছে.")  # "XML file is attached successfully."
                
                # টিউপলের দ্বিতীয় উপাদানটি হল ফাইলের কনটেন্ট (বাইনারি ডেটা)
                file_data = embedded_file_info[1]  # Get the file content (binary data)
                
                # XML ফাইলটি ডিস্কে সংরক্ষণ করুন
                with open(filename, "wb") as f:
                    f.write(file_data)
                print(f"{filename} সফলভাবে সংরক্ষিত হয়েছে.")  # "{filename} has been extracted successfully."
    else:
        print("কোনও এম্বেডেড ফাইল পাওয়া যায়নি।")  # "No embedded files found."

# Example usage
pdf_path = "invoice_with_embedded_xml.pdf"

## For Testing _________________________________
# pdf_path = "without_xml.pdf"
# pdf_path = "with_xml.pdf"
check_pdf_attachments(pdf_path)
