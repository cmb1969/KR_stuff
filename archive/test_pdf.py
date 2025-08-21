import pdfplumber

def test_pdf_reading():
    pdf_path = "KrogerPDFs/060-C2505-83977.pdf"
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Successfully opened PDF with {len(pdf.pages)} pages")
            
            # Print first 200 characters of the first page
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            print("\nFirst 200 characters of the PDF:")
            print("-" * 50)
            print(text[:200])
            
            # Try to find the invoice number
            print("\nLooking for invoice number:")
            if "Invoice #" in text:
                print("Found 'Invoice #' in the text")
                
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_pdf_reading()
