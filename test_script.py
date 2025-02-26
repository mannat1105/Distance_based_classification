import os

def check_files():
    required_files = ["Lab 5-2.ipynb", "README.md"]
    for file in required_files:
        if not os.path.exists(file):
            print(f"Missing: {file}")
        else:
            print(f"Found: {file}")

if __name__ == "__main__":
    check_files()
