import os

def main():
    pdf_path = r"KrogerPDFs\060-C2505-83977.pdf"
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {os.path.abspath(pdf_path)}")
        # List the current working directory
        print("\nCurrent working directory:")
        print(os.getcwd())
        print("\nContents of current directory:")
        print(os.listdir())
        return
    
    # Try to read the file as binary
    try:
        with open(pdf_path, 'rb') as f:
            # Read first 100 bytes to check if it's a PDF
            header = f.read(100)
            if header.startswith(b'%PDF-'):
                print("Success! This appears to be a valid PDF file.")
                print(f"File size: {os.path.getsize(pdf_path) / 1024:.2f} KB")
            else:
                print("Warning: File exists but doesn't appear to be a valid PDF")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

if __name__ == "__main__":
    main()
