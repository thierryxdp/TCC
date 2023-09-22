#Para calcular quantos carros são necessários para uma viagem
#com P pessoas e C capacidade,
#devemos fazer carros=P/C, caso carros == float, arredondar
#para cima
def carros(P,C=5):
    """Calcula quantos carros são necessários para uma viagem,
    dados a quantidade de pessoas P e a capacidade do carro C;
    int, int -> int"""
    c=P/C
    if c == int(c):
        print(c)
    else:
        print (round(c+0.5))