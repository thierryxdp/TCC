def filtraMultiplos(lista,n):
    '''Função que retorna uma nova lista com os elementos da lista original que forem divisiveis por n,
    dado como entrada a lista original. list,int->list'''
	lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
        	lista += [lista[i],]
        i = i + 1
    return lista1