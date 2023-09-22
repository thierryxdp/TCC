def conta_numero(n,matriz):
    """Retorna a quantidade de vezes que um numero inteiro dado como entrada aparece na matriz;
    list,int -> int
    """

    contador = 0
    linhas = len(matriz)
    
    for i in range(linhas):
        if linhas == 0:
            return 0
        colunas = len(matriz[0])
        for j in range(colunas):
            if matriz[i][j] == n:
                contador += 1
                
    return contador