def acima_da_media(lista):
    """Funcao que retorna uma list ordenada com as notas que ficaram acima da media;
    list -> list"""
    
    ntermos = sum(lista)
    qtermos = len(lista)
    media = ntermos//qtermos
    listaNova = list.append(lista, media)
    list.sort(listaNova)
    v1 = list.index(listaNova, media)
    p = v1+1
    
    return lista[p:]