def acima_da_media(lista):
    numero_elem=len(lista)
    media=int(sum(lista)/numero_elem)
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    return lista[posicao+1:]