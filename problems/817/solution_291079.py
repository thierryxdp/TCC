def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    
    list.append(lista,media)
    list.sort(lista)
    
    if lista[media-1]==lista[media]:
        del lista[media-1]
        
    if lista[media+1]==lista[media]:
        del lista[media+1]
    
    a=list.index(lista,media)
    
    return lista[a+1:]