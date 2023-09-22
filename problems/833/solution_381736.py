def conta_numero(n,matriz):
    """Retorna a quantidade de vezes que um numero inteiro dado como entrada aparece na matriz;
    list,int -> int
    """

    contador = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
	
    if matriz == list():
        return 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == n:
                contador += 1
                
    return contador