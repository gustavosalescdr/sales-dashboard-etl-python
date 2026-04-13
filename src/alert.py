def alerta(vendas_baixas):
    if len(vendas_baixas) > 0:
        print("⚠️ ALERTA: Existem vendas abaixo da média!")
        print(vendas_baixas)
    else:
        print("✅ Todas as vendas estão dentro do esperado")