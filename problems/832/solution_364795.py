def eh_quadrada(matriz):
    '''A função retorna True se a matriz for quadrada e
    False se a matriz não for quadrada. list --> bool'''
    
    if len(matriz)==0:
        return True
    
    elif len(matriz)==len(matriz[0]):
      	return True
    
    else:
        return False