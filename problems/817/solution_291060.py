def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=round(soma/quantidade,0)
    
    list.sort(lista)
    del(lista,str.index(media))
    
    
    return lista