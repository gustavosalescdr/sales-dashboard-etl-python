import sqlite3
import pandas as pd

conn = sqlite3.connect('database/vendas.db')

df = pd.read_sql('SELECT * FROM vendas', conn)

print(df)