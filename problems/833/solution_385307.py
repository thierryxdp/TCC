def conta_numero(numero,matriz):
    '''Dado um numero e uma matriz, retorna quantas vezes o numero aparece na matriz.
    int, list -> int'''
    qnt = 0
    j = 0
    i = 0
    while i < len(matriz):
        c = list.count(matriz[j], numero)
        qnt = qnt + c 
        j = j+ 1
        i = i + 1
    return qnt