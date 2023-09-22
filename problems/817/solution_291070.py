def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    
    if media in lista == True:
        lista
    else:
        list.append(lista,media)
    
    list.sort(lista)
    a=list.index(lista,media)
    del lista[:a+1]
    
    return lista