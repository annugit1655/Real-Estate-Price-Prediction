# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
import sidetable
from IPython.display import Markdown, display

# Display Setting
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
import warnings
warnings.filterwarnings("ignore")
# set the decimal places to 2
pd.set_option("display.float_format", "{:.2f}".format)

def display_md(string):
    display(Markdown(string))


# Load dataset 
def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Data loaded successfully!")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")

    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")

    except pd.errors.ParserError:
        print("Error: Unable to parse the CSV file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")