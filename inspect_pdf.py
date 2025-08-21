import pdfplumber

def inspect_pdf(pdf_path):
    print(f"Inspecting PDF: {pdf_path}")
    print("=" * 80)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"\n=== Page {page_num} ===")
            
            # Extract text with layout preserved
            text = page.extract_text()
            print("\nText content:")
            print("-" * 40)
            print(text)
            
            # Show the first few lines with line numbers
            print("\nFirst 20 lines with line numbers:")
            print("-" * 40)
            lines = text.split('\n')
            for i, line in enumerate(lines[:20], 1):
                print(f"{i:2d}: {line}")
            
            # Look for invoice number and coupon description
            print("\nLooking for invoice number and coupon description:")
            print("-" * 40)
            for line in lines:
                if any(term in line for term in ["Invoice", "Coupon", "P4W"]):
                    print(f"Found: {line}")
            
            # Stop after first page for now
            break

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = "KrogerPDFs/060-C2505-83977.pdf"
    
    inspect_pdf(pdf_path)
