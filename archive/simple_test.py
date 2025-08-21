import os

def main():
    # Check current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # List files in current directory
    print("\nFiles in current directory:")
    for f in os.listdir('.'):
        print(f"- {f}")
    
    # Check if KrogerPDFs directory exists
    pdf_dir = "KrogerPDFs"
    print(f"\nChecking for {pdf_dir} directory...")
    if os.path.exists(pdf_dir):
        print(f"Found {pdf_dir} directory!")
        print(f"Contents of {pdf_dir}:")
        for f in os.listdir(pdf_dir):
            print(f"- {f}")
    else:
        print(f"{pdf_dir} directory not found!")

if __name__ == "__main__":
    main()
