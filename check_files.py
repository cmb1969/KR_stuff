import os
from pathlib import Path

def check_directory():
    pdf_dir = Path("KrogerPDFs")
    
    if not pdf_dir.exists():
        print(f"Error: Directory '{pdf_dir}' does not exist.")
        return
    
    print(f"Contents of '{pdf_dir}':")
    print("-" * 50)
    
    for file in pdf_dir.glob("*.pdf"):
        print(f"File: {file.name}")
        print(f"  Exists: {file.exists()}")
        print(f"  Size: {file.stat().st_size / 1024:.2f} KB")
        print(f"  Readable: {os.access(file, os.R_OK)}")
        print()

if __name__ == "__main__":
    check_directory()
