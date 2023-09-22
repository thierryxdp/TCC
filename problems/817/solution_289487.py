def maiores(lista, num):
    """..."""
    L = list.copy(lista)
    list.append(L, num)
    list.sort(L)
    pos = list.index(L, num)
    if L[pos] != L[pos+1]:
        return L[pos+1:]
    else:
        return L[pos+2:]
    
def acima_da_media(lista):
    media = sum(lista)/len(lista)
    return maiores(lista, media)