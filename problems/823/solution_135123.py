def faltante(lista):
    '''Descobre o número faltante dentro da lista
    list->int'''
    list.sort(lista)
    i=0
    
    while i<len(lista):
        if not i==lista[i]-1:
            return i+1
        i=i+1
    	if i==lista[len(lista)]:
        	return i+1