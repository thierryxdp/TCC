def carros(Qtd_Pessoas):
    carros = Qtd_Pessoas//5 +(Qtd_Pessoas%5)/(Qtd_Pessoas%5)
    return int(carros)