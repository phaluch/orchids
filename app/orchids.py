from datetime import datetime, timedelta
from time import sleep
import serial
import pandas as pd

def rowUp(line):
    row = [int(value) for value in line.split(':')]
    row.append(datetime.now())
    return row

def fileName():
    return datetime.strftime(datetime.now(),'%Y%m%d%H%M%S.snappy.parquet')

# Constantes e variáveis
save_interval = timedelta(seconds=10)
columns = ['sensor','value','ts']

# Criando conexão Serial
ser = serial.Serial('COM3',9600)

# Loop principal
t0 = datetime.now()
records = []
while True:
    t1 = datetime.now()
    while ser.in_waiting > 0:
        line = ser.readline().decode().rstrip()
        print(line.split(':'))
        records.append(rowUp(line))
    if t1-t0 > save_interval:
        df = pd.DataFrame(records,columns=columns)
        df.to_parquet(fileName(),compression='snappy')
        t0 = datetime.now()
        records = []
        
