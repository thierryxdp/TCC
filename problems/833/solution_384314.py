def conta_numero(numero: int, matriz: List):
    """ """
    conta = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                conta = conta + 1
    return conta