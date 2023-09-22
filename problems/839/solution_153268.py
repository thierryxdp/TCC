def carros (A, B):
    """ calcula a quantidade de carros necessários dado 
    o número de passageiros (A) e a capacidade de cada 
    carro (B). """
    if A <= B:
        print (1)
    return (A//B)