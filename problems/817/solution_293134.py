def acima_da_media(nota):
    
	media = sum(nota)/len(nota)
    resultado = maiores(nota,media)
	
    if resultado[0] == media:
        del resultado[0]
    
    return resultado
     
def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.index(n)  
    indice_lista = lista.index(n)
    
    return lista[indice_lista+1:]