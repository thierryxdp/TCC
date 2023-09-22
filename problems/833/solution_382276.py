def conta_numero(numero,matriz):
    """essa função conta a quantidade de vezes que um número aparece em uma matriza
int, lista-->int"""
    qtd = 0
    for i in matriz:
        for c in i:
            if c == numero:
                qtd=qtd+1
    return qtd