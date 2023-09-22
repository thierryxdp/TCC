def media_matriz(matriz):
    """funcao que dada uma matriz de inteiros nao vazia, retorna a media dos numeros da matriz com duas casas decimais de precisao
    list(list(int))--->float"""
    n_elementos=len(matriz)*len(matriz[0])
    soma=0
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            soma=soma+ matriz[i][j]
    return round((soma/n_elementos),2)