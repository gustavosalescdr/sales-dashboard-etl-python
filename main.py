from src.extract import extract
from src.transform import transform
from src.load import load
from src.analytics import analisar
from src.alert import alerta

def pipeline():
    df = extract()
    df = transform(df)
    load(df)
    
    vendas_baixas = analisar(df)
    alerta(vendas_baixas)

if __name__ == "__main__":
    pipeline()