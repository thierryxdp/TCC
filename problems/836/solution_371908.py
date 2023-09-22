def busca(setor,matriz):
    '''Recebe um valor string e uma matriz em forma de lista
    e retorna uma lista contendo as informações dos funcionários
    str,list->list'''
    if setor in matriz:
    	lista=[]
    	for i in matriz:
    		if setor in i:
        		list.append(lista,list(i))
    	list.remove(lista[0],setor)
    	return lista
    else:
        return []