import logging
from zipfile import ZipFile
from pathlib import Path
#from src.logger import create_log_path, CustomLogger

with ZipFile('e:/house_price_prediction/Real-Estate-Price-Prediction/data/raw/zipped/house-prices-advanced-regression-techniques.zip','r') as zip_file:
    file_list = zip_file.namelist()
    print('The File List are :', file_list)

def extract_all_file(input_path: Path, output_path: Path):
    with ZipFile(file= input_path) as f:
        f.extractall(path= output_path)