def eh_quadrada(matriz):
    '''Verifica se a matriz é no formato quadrado;
    list(list)->bool'''
    
    if len(matriz)==len(matriz[0]):
        return True
    elif matriz==[]:
    	return True
    else:
        return False