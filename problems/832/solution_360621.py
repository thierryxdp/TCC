def eh_quadrada (matriz):
    vazia=[]
    for i in matriz:
        if len(matriz)==vazia:
            return True
        elif len(matriz)==len(matriz[0]):
        	return True
    	else:
        	return False
'''funcao que recebe uma matriz e retorna 
True se ela for quadrada e False caso contrario
list->bool'''