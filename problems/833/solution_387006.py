def conta_numero(numero,matriz):
    """
    recebe um numero inteiro e uma matriz e retorna a quantidade de
    vezes que aquele numero aparece na matriz.
    """
    vezes=0
    for linha in matriz:
        for elem in linha:
            if elem == numero:
                vezes+=1
    return vezes