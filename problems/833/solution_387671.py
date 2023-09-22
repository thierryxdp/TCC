def conta_numero(numero,matriz):
    """Dado um número de entrada e uma matriz, conta e retorna quantas vezes o número aparece na matriz"""
    i = 0
    for x in matriz:
        for y in x:
            if y==numero:
                qtd=qtd+1
    return qtd