from classes import ParquetReader as pr
reader = pr('../data/')
reader.read_all_parquet_files()
reader.save_smooth_line_chart('linechart.png', sensors=[])