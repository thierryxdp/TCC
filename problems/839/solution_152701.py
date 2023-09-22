#Para calcular quantos carros são necesários para uma viagem
#com P pessoas em um carro de C capacidade,
#devemos fazer carros = P/C, aproximando sempre para cima
#(aproximar o float)
def carros(P,C=5):
    """Cacula o número exato de carros necessários para uma viagem,
    dados a quantidade de pessoas e a capacidade do carro"""
    c=P/C
    return round(c+0.5)