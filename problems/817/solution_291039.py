def acima_da_media(lista):
    
    media = round((sum(lista) / len(lista)))
    lista.append(media)
	lista.sort()    
    cont = lista.index(media)
        
    lista_maiores = lista[cont+1:]
        
    return lista_maiores