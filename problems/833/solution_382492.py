def conta_numero(numero,matriz):
    """essa função conta o indici de aparicao de um número em uma matriza
int, lista-->int"""
    quant = 0
    for x in matriz:
        for v in x:
            if v == numero:
                quant+=1
    return quant