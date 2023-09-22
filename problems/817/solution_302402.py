def acima_da_media(lista_numero):
    n=((sum(lista_numero))/len(lista_numero))
    if n in lista_numero:
        list.sort(lista_numero)
        list.sort(lista_numero)
    	b=list.index(lista_numero,n)
        return b
    else: 
    	list.append(lista_numero, n)
    	list.sort(lista_numero)
    	a=list.index(lista_numero,n)
    	return lista_numero[a+1:]