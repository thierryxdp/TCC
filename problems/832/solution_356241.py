def eh_quadrada(matriz):
    """ Função que recebe uma matriz e retorna True caso a matriz seja quadrada e False caso não seja
    	Uma matriz é quadrada se ela é vazia ou se o número de linhas for igual ao número de colunas
        list->bool
     """
    nlinhas = len(matriz[0])
    if nlinhas == 0:
        return True
    ncolunas = len(matriz[0][0])
    
    if nlinhas==ncolunas:
        return True
    else:
        return False