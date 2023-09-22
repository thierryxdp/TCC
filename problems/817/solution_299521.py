def acima_da_media(L):
    """Função que retorna uma lista com as notas
    que ficaram acima da média.
    list -> list"""
    media = sum(L)/len(L)
    if len(L)==1:
        return []
    if media(L) in L:
        L.sort()
        return L[L.index(media(L))+1:len(L)]
    else:
        L.append(media(L))
        L.sort(L)
        return L[L.index(media(L))+1:len(L)]