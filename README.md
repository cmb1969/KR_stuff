# Kroger PDF Extractor

Extracts structured data from Kroger-related PDFs and exports a clean Excel workbook.

## Features

- Extracts key fields: `Invoice number`, `Coupon description`, and `Campaign description` (code pattern like `P4W2`, chains like `P4W2-P4W4`).
- Finds the items table based on header anchors (e.g., `Line no … Store name`).
- Writes one Excel workbook with a sheet per PDF, including label rows above the table.
- Auto-detects and bolds the table header row; auto-sizes columns.
- Skips tracking of input/output folders in Git; project is streamlined for core use.

## Requirements

- Python 3.8+
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place PDFs in `KrogerPDFs/` (or set `PDF_SETTINGS['pdf_directory']` in `config.py`).
2. Run the processor:

```bash
python pdf_processor.py
```

3. Output Excel: `extracted_data/all_kroger_data.xlsx`
   - Each sheet = one PDF.
   - Top rows: `Invoice Number`, `Coupon Description`, `Campaign Description` (value may be blank if not present).
   - Below: items table with headers and rows.

## Configuration (`config.py`)

- `PDF_FIELDS`:
  - `invoice_number`: uses a strict pattern like `060-C2505-83977`.
  - `coupon_description`: free text after the label.
  - `campaign_description`: constrained by `value_regex` to code tokens (e.g., `P4W2`, `P4W2-P4W4`), preventing accidental capture of table headers.
- `TABLE_CONFIG`:
  - `table_start`: header line that signals the items table (e.g., `Line no`).
  - `table_end`: end anchor (e.g., `Store name`).
  - `table_headers`: leave empty to infer headers from the PDF.
- `PDF_SETTINGS`:
  - Input/output directories and Excel file name.

Adjust labels or regexes if your PDFs vary (e.g., capitalization or alternative wording).

## Repository structure

- Core:
  - `pdf_processor.py`, `config.py`, `requirements.txt`, `.gitignore`, `README.md`
- Archived helper/tests (kept for reference):
  - `archive/` (moved from root: analysis, tests, and utility scripts)
- Not tracked in Git (remain on disk):
  - `KrogerPDFs/`, `extracted_data/`, `__pycache__/`, `*.zip`, `*.xlsx`

## Troubleshooting

- Missing values: You will still see the label rows (e.g., `Campaign Description`) with blank values if not found.
- Table not found: confirm the header row contains `Line no` and the end anchor `Store name`, or adjust `TABLE_CONFIG`.
- Campaign regex too strict/loose: edit `PDF_FIELDS['campaign_description']['value_regex']` accordingly.

## Example console output

```
Found 3 PDF files to process.
Processing 060-C2505-83977.pdf...
Found Invoice number: 060-C2505-83977
Found Coupon description: P4W2-P4W4 BUY 5 SAVE 5 MEGA
Warning: Could not find value for any of labels: ['Campaign description']
Excel: wrote 12 data rows to sheet '060-C2505-83977'
All data has been saved to: extracted_data\all_kroger_data.xlsx
```

## License

MIT
