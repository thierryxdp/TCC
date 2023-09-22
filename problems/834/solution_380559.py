def media_matriz(matriz):
    '''função que dada uma matriz de inteiros
    retorna a média desses números,
    com duas casas decimais'''

    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)