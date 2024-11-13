import fitz  # PyMuPDF

def check_pdf_attachments(pdf_path):
    doc = fitz.open(pdf_path)

    # Check if there are any embedded files
    if doc.embfile_count() > 0:
        print("Embedded files found:")
        for i in range(doc.embfile_count()):
            # Get the embedded file information as a tuple
            embedded_file_info = doc.embfile_get(i)

            # The first element in the tuple is the filename
            filename = str(embedded_file_info[0])  # Convert to string and lowercase

            print(f"File: {filename}")
            
            # Check if the "info.xml" is embedded
            if filename.lower() == "info.xml".lower():
                print("XML file is attached successfully.")
                
                # The second element in the tuple is the file content (binary data)
                file_data = embedded_file_info[1]  # Get the file content (binary data)
                
                # Extract and save the XML file to disk
                with open(filename, "wb") as f:
                    f.write(file_data)
                print(f"{filename} has been extracted successfully.")
    else:
        print("No embedded files found.")

# Example usage
pdf_path = "invoice_with_embedded_xml.pdf"

## For Testing _________________________________
# pdf_path = "without_xml.pdf"
# pdf_path = "with_xml.pdf"
check_pdf_attachments(pdf_path)
