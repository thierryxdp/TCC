def conta_numero(numero, matriz):
    """
"""
    repete = 0
    for n in matriz:
        for x in n:
            if x == numero:
                repete = repete + 1
    return repete