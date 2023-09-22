def eh_quadrada(matriz):
    """ Função que recebe uma matriz e retorna True caso a matriz seja quadrada e False caso não seja
    	Uma matriz é quadrada se ela é vazia ou se o número de linhas for igual ao número de colunas
        list->bool
     """
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    
    if nlinhas == ncolunas:
        return True
    else:
        nlinhas = 0
        ncolunas = 0
        for i in range(len(matriz)):
            nlinhas = nlinhas+1
            for j in range(len(matriz[i])):
                ncolunas = ncolunas + 1
                if nlinhas>=ncolunas or nlinhas<=ncolunas:
                    return False
           
    else:
        return True