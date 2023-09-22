def conta_numero(numero, matriz):
    '''dada uma matriz e um inteiro n, retorna quantas vezes ele aparece na matriz
    int, list -> int'''
    contador = 0
    for linha in matriz:
        for item in linha:
            if item == numero:
                contador += 1
    return contador