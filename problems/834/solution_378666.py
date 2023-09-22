def media_matriz(matriz):
    """função que, dada uma matriz de numeros inteiros não vazia, retorna a média de todos os 
    numeros da matriz;
    list-->int"""
    cont = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in matriz:
        for j in i:
            cont = cont + j
            elementos = linhas*colunas
    return round(cont/elementos,2)