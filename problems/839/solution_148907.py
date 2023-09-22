def carros(Qtd_Pessoas,carro=5):
    carros = Qtd_Pessoas//carro + (Qtd_Pessoas%carro)/(Qtd_Pessoas%carro)
    return int(carros)