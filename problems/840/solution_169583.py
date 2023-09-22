import math
def bolos(A,B,C):
    """
    A função bolo ira retornar quantos bolos joao consegue fazer
    com a quantidade de ingredientes dada nos argumentos, sendo A
    farinha de trigo, B ovos e C colheres de sopa de leite
    int,int,int->float
    """
    qtdA = A/2
    qtdB = B/3
    qtdC = C/5
    
    return int(min(qtdA,qtdB,qtdC))