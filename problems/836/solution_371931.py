def busca(setor,matriz):
    '''Recebe um valor string e uma matriz em forma de lista
    e retorna uma lista contendo as informações dos funcionários
    str,list->list'''
    lista=[]
    for i in matriz:
    	if setor in i:
       		list.append(lista,list(i))
    for j in range(len(lista)):
    	list.remove(lista[j],setor)
    return lista