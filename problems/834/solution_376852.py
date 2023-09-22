def media_matriz(matriz):
    '''funçao que dada uma matriz retorna a media de todos numeros dela'''
    soma = 0
    quantidadesDeNumeros = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            soma = soma + matriz[i][j]
            quantidadesDeNumeros +=1
    return round(soma/quantidadesDeNumeros)