import os

def test_pdf_access():
    pdf_dir = "KrogerPDFs"
    print(f"Checking PDFs in: {os.path.abspath(pdf_dir)}")
    
    # Check if directory exists
    if not os.path.exists(pdf_dir):
        print(f"Error: Directory '{pdf_dir}' does not exist.")
        print("Current working directory:", os.getcwd())
        return
    
    # List PDF files
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    print(f"Found {len(pdf_files)} PDF files.")
    
    if not pdf_files:
        return
    
    # Test reading the first PDF
    first_pdf = os.path.join(pdf_dir, pdf_files[0])
    print(f"\nTesting read access to: {first_pdf}")
    
    try:
        with open(first_pdf, 'rb') as f:
            header = f.read(5)
            if header == b'%PDF-':
                print("Success! This appears to be a valid PDF file.")
                print(f"File size: {os.path.getsize(first_pdf) / 1024:.1f} KB")
            else:
                print("Warning: File exists but doesn't appear to be a valid PDF")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    test_pdf_access()
