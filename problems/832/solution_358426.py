def eh_quadrada(matriz):
    '''função que dada uma matriz como entrada, verifica se a matriz é 
    quadrada;  tuple->bool'''
    if len(matriz)==0:
        return True
	elif int(len(matriz))==int(len(matriz[0])):
		return True
	else:
		return False