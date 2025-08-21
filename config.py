"""
Configuration for PDF data extraction.

This file defines the structure of the data we want to extract from the PDFs.
"""

# Define the expected fields in the PDF
# Format: {"field_name": {"label": "Label in PDF", "type": str/int/float}}
PDF_FIELDS = {
    # Non-regex extraction using labels. The extractor supports value on same line or next line.
    # Use value_regex to pick the correct token near the label (similar to the filename, e.g., 060-C2505-83977)
    "invoice_number": {
        "labels": ["Invoice number"],
        "type": str,
        "value_regex": r"\b\d{3}-[A-Z0-9]{3,}-\d{2,}\b"
    },
    "coupon_description": {"labels": ["Coupon description"], "type": str},
    # Campaign codes often look like AlphaNumberAlphaNumber, e.g., P4W2 or chains like P4W2-P4W4
    "campaign_description": {
        "labels": ["Campaign description"],
        "type": str,
        "value_regex": r"\b(?:[A-Z]\d+[A-Z]\d+)(?:\s*[\-\/&]\s*[A-Z]\d+[A-Z]\d+)*\b"
    },
    # Add more fields as needed based on your PDF structure
}

# Define table structure if there are tabular data in the PDF
TABLE_CONFIG = {
    # Use the header row we saw working earlier
    "table_start": "Line no",
    "table_headers": [],  # let the parser infer headers present under the "Line no ..." header row
    "table_end": "Store name",
    "skip_rows": 0,
    # Expected headers to identify the correct table (order not required)
    "expected_headers": [
        "Line no",
        "UPC",
        "Location",
        "Item description",
        "Item Quanity",
        "Bill Amount",
        "Accrued Amount",
        "Handling rate",
        "PO Number",
        "Store name"
    ],
    # Minimum number of headers that must match to accept a table
    "min_header_matches": 6,
    # Restrict table search to the section whose header contains this text
    "section_anchor": "Associated Promotions",
}

# PDF processing settings
PDF_SETTINGS = {
    "input_dir": "KrogerPDFs",  # Directory containing PDF files
    "output_dir": "extracted_data",  # Where to save extracted data
    "output_format": "excel",  # Changed to 'excel' for single file output
    "combined_output": True,  # Combine all data into a single file
    "output_filename": "all_kroger_data.xlsx"  # Name of the combined output file
}
