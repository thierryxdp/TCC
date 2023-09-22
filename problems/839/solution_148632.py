import math
def carros (p,c=5):
    """Função que calcula a quantidade de carros necessários para uma viagem de amigos, na entrada ela recebe
    a quantidade de pessoas (inteiro) e também pode receber opcionalmente a capacidade do carro (também interiro).
    Já na saída, ele devolve a quantidade de carros a ser utilizado (inteiro), a função faz o arredondamento para cima 
    caso a divisão retorne um valor decimal."""
    veiculos = p/c
    return math.ceil(veiculos)