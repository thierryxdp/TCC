def acima_da_media(lista_nota:list[float])->list[float]:
    media=sum(lista_nota)/3
    lista_nota.sort()
    
    return lista_nota[lista_nota.index(media)+1:]