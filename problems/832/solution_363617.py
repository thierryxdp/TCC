def eh_quadrada(matriz):
    '''Verifica se a matriz é no formato quadrado;
    list(list)->bool'''
    matrizvazia=[]
    
    if len(matriz)==len(matriz[0]):
        return True
    elif len(matriz)==matrizvazia:
    	return True
    else:
        return False