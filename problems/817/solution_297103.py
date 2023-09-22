def acima_da_media(lista):
    """"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.sort()
    
    
    return lista[int(media)+1:]