def eh_quadrada(matriz):
    '''Verifica se a matriz é no formato quadrado;
    list(list)->bool'''
    matrizvazia=[]
    
    if matriz==matrizvazia:
        return True
    elif len(matriz)==len(matriz[0]):
    	return True
    else:
        return False