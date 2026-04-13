import sqlite3

def load(df):
    conn = sqlite3.connect('database/vendas.db')
    df.to_sql('vendas', conn, if_exists='replace', index=False)
    conn.close()