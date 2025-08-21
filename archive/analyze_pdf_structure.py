import os
import sys
import pdfplumber
from pathlib import Path

def analyze_pdf(pdf_path):
    print(f"Analyzing PDF: {pdf_path}")
    print("=" * 80)
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"\n=== Page {page_num} ===")
                
                # Get the raw text
                text = page.extract_text()
                
                # Print first 200 characters
                print("\nFirst 200 characters:")
                print("-" * 40)
                print(text[:200] + "...")
                
                # Print lines containing key terms
                print("\nLines containing key terms:")
                print("-" * 40)
                key_terms = ["invoice", "coupon", "item", "total", "amount", "date"]
                for line in text.split('\n'):
                    line_lower = line.lower()
                    if any(term in line_lower for term in key_terms):
                        print(f"Found: {line}")
                
                # Print table structure
                print("\nTables found:")
                print("-" * 40)
                for i, table in enumerate(page.extract_tables()):
                    print(f"\nTable {i+1}:")
                    for row in table[:5]:  # Show first 5 rows
                        print(" | ".join(str(cell or "").strip() for cell in row))
                
                # Stop after first page for now
                break
                
    except Exception as e:
        print(f"Error analyzing PDF: {str(e)}")

if __name__ == "__main__":
    # Try to use first command line argument, or default to first PDF in KrogerPDFs
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_dir = Path("KrogerPDFs")
        if not pdf_dir.exists():
            print(f"Error: Directory '{pdf_dir}' not found.")
            print(f"Current working directory: {os.getcwd()}")
            sys.exit(1)
            
        pdf_files = list(pdf_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"No PDF files found in {pdf_dir}")
            sys.exit(1)
            
        pdf_path = pdf_files[0]
    
    analyze_pdf(pdf_path)
