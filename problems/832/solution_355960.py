def eh_quadrada1(matriz):
    """ Função que dada uma matriz identifica se a matriz é quadrada ou não.
    	A Função retorna True se a matriz for quadrada e False se não for
        list-> bool
    """
    nlinhas = 0
    ncolunas = 0

    for i in range(len(matriz)):
        nlinhas = nlinhas+1
        for j in range(len(matriz[i])):
            ncolunas = ncolunas + 1
            if matriz[i][j] == []:
                return True
            if nlinhas != ncolunas:
                return False
            else:
                return True