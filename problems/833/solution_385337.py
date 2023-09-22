def conta_numero(n,matriz):
    """Dado uma matriz e um número n, retorna a quantidade de vezes que n
    aparece na matriz:
    list(list)-->int"""
    linha_matriz=len(matriz)
    if matriz==[]:
        return 0
    else:
        coluna_matriz=len(matriz[0])
        contador=0
        for i in range(linha_matriz):
            for j in range(coluna_matriz):
                if matriz[i][j]==n:
                    contador+=1
    return contador