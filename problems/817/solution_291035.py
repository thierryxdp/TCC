def acima_da_media(lista):
    
    media = (sum(lista) / len(lista))    
	lista.sort()    
    cont = lista.index(media)
        
    lista_maiores = lista[media:]
        
    return lista_maiores