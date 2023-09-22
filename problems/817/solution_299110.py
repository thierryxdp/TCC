def acima_da_media(lista_nota:list[float],media:float)->list[float]:
    lista_nota.append(media)
    lista_nota.sort()
    
    return lista_nota