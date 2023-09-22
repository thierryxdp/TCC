def conta_numero(num,matriz):
    """essa função recebe um valor qualquer e uma matriz
     e retorna quantas aparições daquele número ocorrem
     dentro da matriz;
     int,list-->int"""
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                contador += 1
    return contador