import os
import pandas as pd
from matplotlib import pyplot as plt

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

    def hourly_moving_average(self):
        # Group the dataframe by 'sensor' and 'ts', then calculate the moving average of 'value' with a window of 1 hour
        df_hourly = self.df_combined.groupby(['sensor', pd.Grouper(key='ts', freq='4H')])['value'].mean().reset_index()
        return df_hourly

    def save_smooth_line_chart(self, filename, sensors=[]):
        # Get the hourly moving average dataframe
        df_hourly = self.hourly_moving_average()
        
        # Get a list of unique sensor values in the dataframe
        if not sensors:
            sensors = df_hourly['sensor'].unique()
        
        # Create a new figure and axis object
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot a smooth line chart for each sensor in the dataframe
        for sensor in sensors:
            data = df_hourly[df_hourly['sensor'] == sensor]
            ax.plot(data['ts'], data['value'], label=sensor)
        
        # Set the axis labels and legend
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.legend()
        
        # Save the figure to a .png file
        plt.savefig(filename)