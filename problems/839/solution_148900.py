def carros(Qtd_Pessoas,carro=5):
    carros = Qtd_Pessoas//carro + (Qtd_Pessoas%carro)+1/(Qtd_Pessoas%carro)+1
    return int(carros)