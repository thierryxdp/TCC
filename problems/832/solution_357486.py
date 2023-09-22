def eh_quadrada(matriz):

    """ Função que retorna um valor booleano que afirma se uma matriz é quadrada
        ou não. Matrizes quadradas possuem o mesmo número de linhas e colunas.
        Por definição, uma matriz vazia é considerada quadrada.
        list -> bool
    """

    if len(matriz) == 0:
        return True

    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False