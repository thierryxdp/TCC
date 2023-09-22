def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=ceil(soma/quantidade)
    
    list.sort(lista)
    
    return lista(all>media)