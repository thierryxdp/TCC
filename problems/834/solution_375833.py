def media_matriz(matriz):
    """Retorna a media de todos os numeros da raiz.list-->float"""
    soma=0
    for i in matriz:
        for j in i:
            soma=soma+j
    c=len(matriz)*len(matriz[0])
    d=soma/c
    return round(d,2)