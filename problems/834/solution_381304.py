def media_matriz(matriz):
    ''' funcao que dada uma matriz de inteiros
    retorna a media desses numeros, com suas casas
    decimais'''
    
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)