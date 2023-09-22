def conta_numero(numero, matriz):
    """ função que recebe um numero e uma matriz e devolve quantas vezes o numero aparece na matriz
    	entrada: int, lista
        saida: int
    """
    
    conta = 0
    
    for i in matriz:
        conta += list.count(i,numero)    
    return conta