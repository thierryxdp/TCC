def melhor_volta(matriz):
    retorno = (0,float('inf'),0)
    for linhas in range(6):
        for colunas in range(10):
            if matriz[linhas][colunas] < retorno[1]:
            retorno = (linhas+1,matriz[linhas][colunas],colunas+1)
    return float('inf')