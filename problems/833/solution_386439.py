def conta_numero(numero,matriz):
    """função que dado um numero inteiro e uma matriz conta e retorna quantas vezes aquele numero aparece na matriz; int,matriz-->int"""
    qtd = 0
    for l in matriz:
        for n in l:
            if n == numero:
                qtd = qtd + 1
    return qtd