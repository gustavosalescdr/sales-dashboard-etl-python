def analisar(df):
    media = df['total'].mean()
    
    vendas_baixas = df[df['total'] < media]
    
    print(f"📊 Média de vendas: {media}")
    
    return vendas_baixas