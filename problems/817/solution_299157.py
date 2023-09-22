def acima_da_media(lista):
    """Função que retorna uma lista ordenada com as notas dos alundos que ficaram acima da média
    list -> list"""
    
    media = sum(lista) / len(lista)
    
    if media in lista:
        
        lista.sort()
        indice = lista.index(media)
        
        return lista[indice + 1:]
    
    else:
        
        lista = lista + [media]
        lista.sort()
        indice = lista.index(media)
        
        return lista[indice + 1:]