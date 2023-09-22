def busca(setor,matriz):
    '''Recebe um valor string e uma matriz em forma de lista
    e retorna uma lista contendo as informações dos funcionários
    str,list->list'''
    lista=[]
    for i in matriz:
        if str(setor) in i:
            lista.append(i)
    	for j in lista:
            if str(setor) in j:
            	lista.remove(setor)
    return lista