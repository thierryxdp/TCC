def maiores(lista, n):
    
    if n in lista:
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        
        return lista1
    
	else:
        
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        
        return lista1

def acima_da_media(lista):
    '''Recebe uma lista de notas (lista), e retorna
    uma lista ordenada com as notas que ficaram
    acima da media
    
    list -> list
    '''
    media = int(sum(lista)/len(lista))
    
    return maiores(lista, media)