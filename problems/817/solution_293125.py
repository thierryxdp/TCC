def acima_da_media(nota):
    
	media = sum(nota)/len(nota)
    
    return maiores(nota,media)

def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.index(n)  
    indice_lista = lista.index(n)
    
    return lista[indice_lista+1:]