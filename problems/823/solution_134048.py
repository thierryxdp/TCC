def faltante(lista):
    '''
    '''
    contador = 1
    while contador<len(lista-1):
       	contador += 1
        if lista[contador] != lista[contador-1] + 1:
        	return contador
       	return -1