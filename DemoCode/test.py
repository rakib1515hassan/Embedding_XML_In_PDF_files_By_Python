import fitz  # PyMuPDF

def check_pdf_attachments(pdf_path):
    doc = fitz.open(pdf_path)

    # Check if there are any embedded files
    if doc.embfile_count() > 0:
        print("Embedded files found:")
        for i in range(doc.embfile_count()):
            embedded_file = doc.getEmbeddedFile(i)
            filename = embedded_file[0]  # Extract file name
            
            print(f"File: {filename}")
            
            # Check if the "info.xml" is embedded
            if filename.lower() == "info.xml".lower():
                print("XML file is attached successfully.")
                
                # Extract and save the XML file to disk
                file_data = embedded_file[1]  # File content
                with open(filename, "wb") as f:
                    f.write(file_data)
                print(f"{filename} has been extracted successfully.")
    else:
        print("No embedded files found.")

# Example usage
pdf_path = "invoice_with_embedded_xml.pdf"
check_pdf_attachments(pdf_path)
