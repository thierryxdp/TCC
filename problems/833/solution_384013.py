def conta_numero(numero,matriz):
    '''função que conta quantas vezes o valor de entrada
    número se repete na matriz de entrada; float,list -> int
    '''
    counter = 0
    i = 0
    j = 0
    n_linhas = len(matriz)
    while i in range(n_linhas):
        n_colunas = len(matriz[i])
        while j in range(n_colunas):
            if matriz[i][j] == numero:
                counter += 1
                i += 1
                j += 1
        return counter