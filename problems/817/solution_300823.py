def acima_da_media(lista):
    if len(lista) == 1:
        return []
    else:
        a = sum(lista)/len(lista)
        list.append(lista,a)
        list.sort(lista)
        lista = lista[list.index(lista,a)+1:]
        return lista