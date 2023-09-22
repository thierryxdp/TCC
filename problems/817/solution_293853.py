def acima_da_media(lista):
    """Funcao que retorna uma list ordenada com as notas que ficaram acima da media;
    list -> list"""
    
    ntermos = sum(lista)
    qtermos = len(lista)
    media = ntermos//qtermos
    lista1 = list.append(lista, media)
    list.sort(lista1)
    v1 = list.index(lista1, media)
    p = v1+1
    
    return lista[p:]