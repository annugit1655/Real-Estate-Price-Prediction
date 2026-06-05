import logging
from zipfile import ZipFile
from pathlib import Path

# Extract all zipped files
def extract_all_file(input_path:Path, output_path:Path):
    with ZipFile(file= input_path) as f:
        f.extractall(path= output_path)

def main():
    # current file path 
    current_path = Path(__file__)
    # root directory path
    root_path = current_path.parent.parent.parent
    # raw data directory path
    raw_data_path = root_path / 'data' / 'raw'
    # output path for the zip files
    output_path = raw_data_path / 'extracted'
    # make the directory for the path
    output_path.mkdir(parents=True,exist_ok=True)
    # input path for zip files
    zipped_path = raw_data_path / 'zipped'
    
    print(zipped_path)#house-prices-advanced-regression-techniques.zip)
    
    # Extract the files
    extract_all_file(input_path = zipped_path/ 'house-prices-advanced-regression-techniques.zip',output_path = output_path)

# call the main function
if __name__ == "__main__":
    main()

