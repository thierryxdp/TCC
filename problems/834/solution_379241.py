def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia,
    retorna a média dos elementos da matriz;
    list(list[str]) -> float'''
    cont_elem=0
    soma_elem=0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
         for j in range(colunas):
             soma_elem=soma_elem+matriz[i][j]
             cont_elem=cont_elem+1
    return round(soma_elem/cont_elem,2)