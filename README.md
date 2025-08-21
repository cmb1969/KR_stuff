# PDF Data Extractor

This Python script extracts structured data from PDF files, focusing on specific fields and tables within the documents.

## Features

- Extracts text and tabular data from PDF files
- Configurable field extraction using regex patterns
- Handles multiple PDF files in a directory
- Saves results in CSV or Excel format
- Processes both individual fields and tabular data

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Edit the `config.py` file to define:

- `PDF_FIELDS`: The fields you want to extract from the PDFs
- `TABLE_CONFIG`: Configuration for extracting tabular data
- `PDF_SETTINGS`: Input/output directories and file formats

## Usage

1. Place your PDF files in the `KrogerPDFs` directory (or update the path in `config.py`)
2. Run the script:

```bash
python pdf_processor.py
```

3. The extracted data will be saved in the `extracted_data` directory
   - Individual PDF results: `[filename].csv` and `[filename]_items.csv`
   - Combined results: `combined_results.csv`

## Customization

### Adding New Fields

To extract additional fields, add them to the `PDF_FIELDS` dictionary in `config.py`:

```python
PDF_FIELDS = {
    "field_name": {
        "label": "Label in PDF",  # The exact text that appears before the value
        "type": str  # Data type (str, int, float)
    },
    # Add more fields as needed
}
```

### Table Extraction

Modify the `TABLE_CONFIG` in `config.py` to match your PDF's table structure:

```python
TABLE_CONFIG = {
    "table_start": "Header Text",  # Text that marks the start of the table
    "table_headers": ["Col1", "Col2", ...],  # Expected column headers
    "table_end": None  # Text that marks the end of the table (if any)
}
```

## Output

The script generates two types of output files for each PDF:

1. `[filename].csv`: Contains the extracted fields
2. `[filename]_items.csv`: Contains the tabular data (if any)

A combined results file is also created with data from all processed PDFs.

## Troubleshooting

- If fields aren't being extracted correctly, verify the field labels in the PDF match those in `config.py`
- For table extraction issues, check the table structure and update the `TABLE_CONFIG` accordingly
- Enable debug mode by adding `print` statements in the code to inspect the extracted text

## License

This project is open source and available under the [MIT License](LICENSE).
