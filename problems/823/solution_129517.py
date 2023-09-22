def faltante(lista):
    '''retorna o número da peça faltante, list->int'''
    i=0
    list.sort(lista)
    while i<len(lista):
    	if list[i]==i+1:
        	i=i+1
    return lista[i]+1