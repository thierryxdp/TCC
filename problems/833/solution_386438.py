def conta_numero(numero,matriz):
    """função que dado um numero inteiro e uma matriz conta e retorna quantas vezes aquele numero aparece na matriz; int,matriz-->int"""
    qtd = 0
    for 1 in matriz:
        for n in 1:
            if n == numero:
                qtd = qtd + 1
    return qtd