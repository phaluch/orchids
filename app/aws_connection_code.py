import awswrangler as wr
import pandas as pd
import boto3
from pyathena import connect

keys = ['aws_access_key_id', 'aws_secret_access_key']
with open('creds.txt') as f:
    creds = {key:value.replace('\n','') for key, value in zip(keys,f.readlines())}

session = boto3.Session(
    aws_access_key_id=creds['aws_access_key_id'],
    aws_secret_access_key=creds['aws_secret_access_key'],
    region_name='us-east-1'
)


wr.s3.to_parquet(

    df=pd.DataFrame({

        'col': [1, 2, 3],

        'col2': ['A', 'A', 'B']

    }),

    path='s3://database-do-athena/athena/erau/tb_exemplo/',
    boto3_session = session,

    dataset=True,

    database='erau',  # Athena/Glue database

    table='tb_exemplo'  # Athena/Glue table

)

conn = connect(s3_staging_dir='s3://database-do-athena/resultados/',
               region_name='us-east-1',
               aws_access_key_id=creds['aws_access_key_id'],
                aws_secret_access_key=creds['aws_secret_access_key'])