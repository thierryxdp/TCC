def conta_numero(numero, matriz):
    """ função que recebe um numero e uma matriz e devolve quantas vezes o numero aparece na matriz
    	entrada: int, lista
        saida: int
    """
    conta = list.count(numero)
    if numero in matriz:
        return conta