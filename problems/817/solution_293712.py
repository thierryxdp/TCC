def acima_da_media(lista):
    media = int(sum(lista)/len(lista))
    lista[0:0] = [media]
    list.sort(lista)
    maiores = lista[(list.index(lista,media))+1:]
    return maiores