def acima_da_media(lista: list) -> list:
    
    list.sort(lista)
    
    a = sum(lista)//len(lista)
    
    list.append(lista, a)
    
    list.sort(lista)
    
	del lista[:list.index(lista, a)]
    
    if list.count(lista, a) > 1:
        list.remove(lista, a)
        list.remove(lista, a)
        list.remove(lista, a)
        
    return lista