def acima_da_media(lista):
    '''
    Funçao que recebe uma lista e retorna outra lista
    com os numeros que estao acima da media da lista
    list -> list
    '''
    m=sum(lista)/len(lista)
    list.insert(lista,0,m)
    list.sort(lista)
   

	if int(m) == lista(list.index(lista,m)+1):
    	del lista[0:list.index(lista,m)+2]
    	return lista
    else:
    	del lista[0:list.index(lista,m)+1]
    	return lista