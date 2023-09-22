def media_matriz(matriz):
    """dada uma matriz de inteiros não vazia, a função retorna a média
entre os números da matriz.
list-->float

Parâmetros
matriz: matriz de números inteiros e não vazia
nlinhas: número de linhas da matriz
ncolunas: número de colunas da matriz
nelementos: número de elementos da matriz
indice1: índice referente ao primeiro while
indice2: índice referente ao segundo while
media: média dos elementos antes de arrendondar
"""
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    nelementos=nlinhas*ncolunas
    acumulador=0
    indice1=0
    while indice1<nlinhas:
        indice2=0
        while indice2<ncolunas:
            acumulador=acumulador+matriz[indice1][indice2]
            indice2=indice2+1
        indice1=indice1+1
    media=acumulador/nelementos
    return round(media,2)