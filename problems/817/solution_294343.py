def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com as notas que
    ficaram acima da média
    lista=list->list'''
    x = sum(lista)//len(lista)
    if x in lista:
    	list.sort(lista)
    	z = list.index(lista,x)
    	return lista[z+1:]
    else:
        list.append(lista,x)
        list.sort(lista)
        z = list.index(lista,x)
        return lista[z+1:]