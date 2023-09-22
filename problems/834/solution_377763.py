def media_matriz(matriz):
    """funcao que calcula a media de uma matriz
    entrada matriz saida float"""
    c=range(len(matriz))*range(len(matriz[0]))
    soma=0
    i=0
    while i<range(len(matriz)):
        s=sum(matriz[0])
        soma+=s
        i+=1
        return soma/c