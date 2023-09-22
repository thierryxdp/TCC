def media_matriz(matriz):
    """funcao que calcula a media de uma matriz
    entrada matriz saida float"""
    c=range(len(matriz))
    d=range(len(matriz[0]))
    z=5    
    i=0
    soma=0
    while i<c:
        s=sum(matriz[i])
        soma+=s
        i+=1
        return soma/z