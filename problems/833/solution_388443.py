def conta_numero(numero, matriz):
    """
"""
    repete = 0
    for n in range(len(matriz)):
        for x in matriz[0]:
            if x == numero:
                repete = repete + 1
    return repete