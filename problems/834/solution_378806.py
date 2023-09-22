def media_matriz(matriz):
    '''retorna a media de todos os numeros da matriz, sendo ela formadada de inteiros e nao vazia;
    matriz->float'''
    soma=0
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            contador=contador+1
    return round(soma/contador,2)