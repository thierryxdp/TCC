def matriz(matriz,n):
    """ Dada uma matriz m, multiplica todos os elementos de m pelo número n
    list,int -> list"""
    M = []
    for linha in range(len(matriz)):
        coluna = []
        for elemento in range(len(matriz[0])):
            coluna.append(0)
        M.append(coluna)
    for linha in range(len(M)):
        for coluna in range(len(M[0])):
            M[linha][coluna] = matriz[linha][coluna]*n
   return M