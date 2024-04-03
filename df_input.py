import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('MK01.csv')

# MySQL connection settings
host = 'localhost'
port = '3306'
user = 'root'
password = '0000'
database = 'state'
charset = 'utf8'

# Create MySQL connection string
connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'

# Create SQLAlchemy engine
engine = create_engine(connection_string)
df.to_sql('usertable', engine, if_exists='replace', index=False)
print("Data inserted successfully.")