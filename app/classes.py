import os
import pandas as pd

class ParquetReader:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.file_list = []
        self.df_list = []
        self.df_combined = pd.DataFrame()

    def get_file_list(self):
        self.file_list = [os.path.join(self.dir_path, file) for file in os.listdir(self.dir_path) if file.endswith('.parquet')]

    def read_parquet_files(self):
        self.df_list = [pd.read_parquet(file) for file in self.file_list]

    def combine_dataframes(self):
        self.df_combined = pd.concat(self.df_list, ignore_index=True)

    def read_all_parquet_files(self):
        self.get_file_list()
        self.read_parquet_files()
        self.combine_dataframes()

    def print_combined_dataframe(self):
        print(self.df_combined)
