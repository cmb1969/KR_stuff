import os
import sys
import platform

def check_environment():
    print("Python Environment Check")
    print("=" * 50)
    
    # Python information
    print("\nPython Version:")
    print(f"Python {sys.version}")
    print(f"Executable: {sys.executable}")
    
    # Platform information
    print("\nSystem Information:")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Check KrogerPDFs directory
    print("\nChecking KrogerPDFs directory:")
    pdf_dir = os.path.join(os.getcwd(), "KrogerPDFs")
    print(f"Path: {pdf_dir}")
    
    if os.path.exists(pdf_dir):
        print("Directory exists")
        print("\nContents of KrogerPDFs:")
        try:
            files = os.listdir(pdf_dir)
            for file in files:
                file_path = os.path.join(pdf_dir, file)
                print(f"- {file} (Size: {os.path.getsize(file_path) / 1024:.2f} KB)")
        except Exception as e:
            print(f"Error listing directory: {str(e)}")
    else:
        print("Directory does not exist")
    
    # Check file permissions
    print("\nFile Permissions:")
    test_file = os.path.join(pdf_dir, "060-C2505-83977.pdf") if os.path.exists(pdf_dir) else ""
    if test_file and os.path.exists(test_file):
        print(f"Checking permissions for {test_file}:")
        print(f"- Readable: {os.access(test_file, os.R_OK)}")
        print(f"- Writable: {os.access(test_file, os.W_OK)}")
        print(f"- Executable: {os.access(test_file, os.X_OK)}")
    else:
        print("Test file not found")

if __name__ == "__main__":
    check_environment()
