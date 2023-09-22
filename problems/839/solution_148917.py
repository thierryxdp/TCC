def carros(Qtd_Pessoas,carro=5):
    mais = 0
    if Qtd_Pessoas%carro > 0:
        mais += 1
    carros = int(Qtd_Pessoas/carro) + mais
    return carros