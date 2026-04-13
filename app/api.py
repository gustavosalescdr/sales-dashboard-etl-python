from flask import Flask, jsonify, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 🔹 Rota para ver todas as vendas
@app.route('/vendas')
def vendas():
    conn = sqlite3.connect('database/vendas.db')
    df = pd.read_sql('SELECT * FROM vendas', conn)
    conn.close()

    return jsonify(df.to_dict(orient='records'))


# 🔹 Rota para ver vendas abaixo da média
@app.route('/alertas')
def alertas():
    conn = sqlite3.connect('database/vendas.db')
    df = pd.read_sql('SELECT * FROM vendas', conn)

    media = df['total'].mean()
    vendas_baixas = df[df['total'] < media]

    conn.close()

    return vendas_baixas.to_json(orient='records')


if __name__ == '__main__':
    app.run(debug=True)
@app.route('/resumo')
def resumo():
    conn = sqlite3.connect('database/vendas.db')
    df = pd.read_sql('SELECT * FROM vendas', conn)

    total_vendas = df['total'].sum()
    media = df['total'].mean()

    conn.close()

    return jsonify({
        "total_vendas": total_vendas,
        "media_vendas": media
    })