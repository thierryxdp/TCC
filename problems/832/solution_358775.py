def eh_quadrada(matriz):
    """ Função que identifica se uma matriz é quadrada; list-> bool"""
    nlinhas= len(matriz)
    ncolunas= len(matriz[0])
	if nlinhas ==ncolunas:
        return True
    elif matriz==[]:
        return True
    else:
        return False