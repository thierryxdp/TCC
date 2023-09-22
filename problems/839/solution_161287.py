def carros(p,cc=5):
    "função que calcula o número de carros necessários para realizar uma viagem, dado como entrada apenas a quantidade de pessoas se o carro comportar no mácimo 5 passageiro, se não dar de entrada a capacidade do carro também." 
    import math
    Qtdcarros= p/cc
    return math.ceil(Qtdcarros)