def conta_numero(numero,matriz):
    '''dado um número inteiro e uma matriz de inteiros, retorna quantas vezes
    esse número aparece na matriz;
    int, list --> int'''
    vezes = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                vezes = vezes + 1
    return vezes