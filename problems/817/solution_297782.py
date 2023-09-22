def acima_da_media(lista):
    quant = int(lista.count(lista,'')+1)
    media = int(sum(lista))/quant
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media)+1:]