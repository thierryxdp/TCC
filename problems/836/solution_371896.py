def busca(setor,matriz):
    
    '''Recebe um valor string e uma matriz em forma de lista
    e retorna uma lista contendo as informações dos funcionários
    str,list->list'''
    lista=[]
    for i in matriz:
    	if setor in i:
        	lista=lista+list(i)
        	list.remove(lista,setor)
    return [lista]