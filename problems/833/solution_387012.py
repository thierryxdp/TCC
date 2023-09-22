def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz,
    retorna quantas vezes aquele número aparece
    na matriz.
    int, list -> int'''
    qnt = 0
    for i in matriz:
        for j in i:
            if i[j] == numero:
                qnt += 1
    return qnt