def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    
    list.sort(lista)
    if media in lista == True:
    	del(lista[:str.index(media)])
    
    return lista