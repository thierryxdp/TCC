def acima_da_media(lista_nota:list[float])->list[float]:
    lista_nota.append(5)
    lista_nota.sort()
    
    return lista_nota[lista_nota.index(5)+1:]