from pdf_processor import PDFProcessor
from config import PDF_SETTINGS

from pathlib import Path

def main():
    # Create a PDF processor instance
    processor = PDFProcessor(PDF_SETTINGS)
    
    # Process a single PDF file
    pdf_path = Path("KrogerPDFs/060-C2505-83977.pdf")
    
    # Extract the data
    data = processor.process_pdf(pdf_path)
    
    # Print the extracted data
    print("\nExtracted Data:")
    print("-" * 50)
    for key, value in data.items():
        if key != 'items':
            print(f"{key}: {value}")
    
    # Print table data if any
    if 'items' in data and data['items']:
        print("\nExtracted Table Data:")
        print("-" * 50)
        for i, item in enumerate(data['items'][:5], 1):  # Show first 5 items
            print(f"Item {i}: {item}")
        if len(data['items']) > 5:
            print(f"... and {len(data['items']) - 5} more items")
    
    # Save the results
    processor.save_results(data, "test_output")
    print("\nResults have been saved to the 'extracted_data' directory.")

if __name__ == "__main__":
    main()
