def media_matriz(matriz):
    """funcao que calcula a media de uma matriz
    entrada matriz saida float"""
    c=len(matriz)
    d=len(matriz[0])
    z=d*c    
    soma=0
    i=0
    while i<len(matriz):
        s=sum(matriz[i])
        i=i+1
    return s/z