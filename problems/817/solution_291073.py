def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    
    if float(media)==int(media):
        media=int(media)
    
    if media in lista == True:
        lista
    else:
        list.append(lista,media)
    
    list.sort(lista)
    a=list.index(lista,media)
    
    return lista[a+1:]