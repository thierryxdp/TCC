def media_matriz(matriz):
    '''Retorna a media de todos os numeros
    da matriz, com precisao de duas casas
    list --> float'''
    soma = 0
    qntd = 0
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma += j
            qntd += 1
    return soma / qntd