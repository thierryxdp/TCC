#Calcula quantos carros é necessário para transportar um número p de passageiros.
def carros(p,v=5):
    capacidade=p/v
    return ceil(capacidade)