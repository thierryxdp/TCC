def media_matriz(matriz):
    '''Função que retona a média aritimética dos 
    elementos de uma matriz; recebe como parâmetro
    uma matriz dada pelo usuário; list(list)-->Float'''
    count=0
    soma=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            count+=1
    return round(soma/count,2)