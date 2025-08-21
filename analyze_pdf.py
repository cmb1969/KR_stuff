import pdfplumber
from pprint import pprint

def analyze_pdf_structure(pdf_path):
    """Analyze the structure of a PDF and print text content with coordinates."""
    print(f"Analyzing PDF: {pdf_path}")
    print("-" * 80)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"\n=== Page {page_num} ===")
            
            # Extract text with positions
            words = page.extract_words(keep_blank_chars=True, x_tolerance=2, y_tolerance=2)
            
            # Print words with their positions
            print("\nText with coordinates (x0, top, x1, bottom, text):")
            print("-" * 80)
            for word in words[:50]:  # Print first 50 words to avoid too much output
                print(f"{word['x0']:.1f}, {word['top']:.1f}, {word['x1']:.1f}, {word['bottom']:.1f}: {word['text']}")
            
            # Extract and print tables if any
            tables = page.extract_tables()
            if tables:
                print("\nFound tables:")
                for i, table in enumerate(tables, 1):
                    print(f"\nTable {i}:")
                    for row in table[:5]:  # Print first 5 rows of each table
                        print(row)
                    if len(table) > 5:
                        print(f"... and {len(table) - 5} more rows")
            
            # Extract and print text blocks
            print("\nText blocks:")
            print("-" * 80)
            text = page.extract_text()
            print(text[:1000] + "..." if len(text) > 1000 else text)
            
            # For the first page, also try to find the coupon description
            if page_num == 1:
                print("\nLooking for coupon description:")
                # Look for text that matches the pattern you described
                coupon_pattern = r'P\d+W\d+-P\d+W\d+.*?MEGA'
                matches = re.findall(coupon_pattern, text)
                if matches:
                    print("Found potential coupon description:", matches[0])
            
            # Stop after first page for now
            break

if __name__ == "__main__":
    import re
    import sys
    
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = "KrogerPDFs/060-C2505-83977.pdf"  # Default to the file you mentioned
    
    analyze_pdf_structure(pdf_path)
