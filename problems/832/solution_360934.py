def eh_quadrada(matriz):
    '''retorna True ou False se a matriz é quadrada ou nao
    list->bool'''
    
    nlinha= len(matriz)
    ncoluna= len(matriz[[0]])
    	
  	if nlinha == ncoluna:
        return True
    else:
        return False