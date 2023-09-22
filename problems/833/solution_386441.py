def conta_numero(numero,matriz):
    """dado um numero inteiro e uma matriz de inteiros, retorna quantas vezes o numero aparece na matriz; int, list -> int"""
    a=0
    for x in matriz:
        for y in x:
            if y==numero:
                a=a+1
    return a