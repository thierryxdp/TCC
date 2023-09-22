def acima_da_media(lista: list) -> list:
    
    list.sort(lista)
    
    a = (sum(lista)/len(lista)) + "a"
    
    list.append(lista, a)
    
    list.sort(lista)
    
	del lista[:list.index(lista, a)]
    
    return lista