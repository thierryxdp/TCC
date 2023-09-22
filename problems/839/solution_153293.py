import math

def carros (A, B=4):
    """ calcula a quantidade de carros necessários dado 
    o número de passageiros (A) e a capacidade de cada 
    carro (B). """
    if A <= B:
        print (1)
    if A >> B:
        return A//B
    return (A//B)