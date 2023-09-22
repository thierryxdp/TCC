def eh_quadrada(matriz):
    '''Dada uma lista de sub-listas que representa uma matriz 
    retorna se a matriz é quadrada.
    list -> bool'''
    
    linhas = len(matriz)
    if linhas != 0:
    	return linhas == len(matriz[0])
    else:
        return True