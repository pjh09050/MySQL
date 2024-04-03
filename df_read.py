import pandas as pd
from sqlalchemy import create_engine

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

# Define SQL query to select all data from the "userTable" table
query = "SELECT * FROM userTable"

# Use pandas to read data from MySQL into DataFrame
df = pd.read_sql(query, engine)

# Display the DataFrame
print(df)