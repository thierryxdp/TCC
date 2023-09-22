def faltante(lista):
    '''retorna o número da peça faltante, list->int'''
    i=0
    while i<len(lista):
    	if lista[i]<lista[i+1]:
        	i=i+1
        if lista[i]+2==lista[i+1]:
            return i-1