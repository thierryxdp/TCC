def eh_quadrada(matriz):
    """ Função que dada uma matriz identifica se ela é ou não quadrada
    	list-> bool
    """
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    
    if nlinhas and ncolunas == [ ]:
        return True