def acima_da_media(lista):
    
    list.append(lista, sum(lista)/len(lista))
    list.sort(lista)
    
    
    if list.count(lista, sum(lista)/len(lista)) ==1:
    	return lista[list.index(lista, sum(lista)/len(lista))+1:]
    
    else:
        return lista[list.index(lista, sum(lista)/len(lista))+2:]