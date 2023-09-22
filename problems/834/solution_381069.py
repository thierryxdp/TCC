def  media_matriz(matriz):
    '''funcao que dada uma matriz de inteiros nao vazia,
    retorna a media de todos os numeros da matriz;
    list(list)-->int'''
    soma=0
    denominador=0
    for i in range(len(matriz)):
        denominador=denominador+len(matriz[i])
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
    return soma/denominador