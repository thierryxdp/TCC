def media_matriz(matriz):
    '''Dada uma matriz, retorne a média de todos os números;list->int'''
    soma=0
    numero=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            numero=numero+1
    return round(soma/numero,2)