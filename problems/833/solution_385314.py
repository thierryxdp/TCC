def conta_numero(numero,matriz):
    '''Retorna quantas vezes numero aparece em matriz
int,list -> int'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    contador=0
    for i in range(linhas):
        for j in range(colunas):
            if numero==matriz[i][j]:
                contador=contador+1
    return contador