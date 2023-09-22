def conta_numero(numero,matriz):
    '''Função que conta e retorna quantas vezes um
    determinado número aparece numa matriz.
    Parâmetros: int,list -> int'''
    if matriz == []:
        return 0
    nlin = len(matriz)
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j] == numero:
                contador+=1
    return contador