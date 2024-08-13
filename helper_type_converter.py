#helper to work with 00_data_prep to quickly convert datatypes
import pandas as pd

def convert_to_datetime(input_df, input_column):
    input_df[input_column] = pd.to_datetime(input_df[input_column], format = 'mixed')

def convert_to_num(input_df, input_column):
    input_df[input_column] = pd.to_numeric(input_df[input_column], errors='coerce')