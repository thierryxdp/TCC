def eh_quadrada(matriz):
    'dado uma matriz retorna se é quadrada ou não' 
    if len(matriz)==0:
    	return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False