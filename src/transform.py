def transform(df):
    df = df.dropna()
    df['total'] = df['quantidade'] * df['preco']
    return df