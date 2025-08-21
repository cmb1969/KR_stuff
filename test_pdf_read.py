import os

def main():
    # Try to read a PDF file
    pdf_dir = "KrogerPDFs"
    if not os.path.exists(pdf_dir):
        print(f"Error: Directory '{pdf_dir}' does not exist.")
        return
    
    # List PDF files
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return
    
    pdf_path = os.path.join(pdf_dir, pdf_files[0])
    print(f"Trying to read: {pdf_path}")
    
    # Try to read the file as binary
    try:
        with open(pdf_path, 'rb') as f:
            header = f.read(5)
            is_pdf = header == b'%PDF-'
            print(f"File exists. Is PDF: {is_pdf}")
            print(f"File size: {os.path.getsize(pdf_path) / 1024:.1f} KB")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    main()
