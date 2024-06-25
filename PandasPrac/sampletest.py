import pyodbc
import pandas as pd


server = 'sqlprac10.database.windows.net'
database = 'sql'
username = 'pubjoe'
password = 'joemathew912!'
driver = '{SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

query = "SELECT * FROM Housing"

df = pd.read_sql(query,conn)

conn.close()

df.info()                                       