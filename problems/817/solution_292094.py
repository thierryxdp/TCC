def acima_da_media(lista):
    """Função que calcula a media dada uma lista de entrada e retorna os numeros aciama da media
    list -> list"""
    media = sum(lista)/len(lista)
    
    lista1 = lista+[media]
    
    list.sort(lista1)
    
    posicao = list.index(lista1,media)
    
    lista_media = lista1[posicao+1:]
    
    if media in lista_media:
    	
        list.remove(lista_media, media)
        
        return lista_media
    
    return lista_media