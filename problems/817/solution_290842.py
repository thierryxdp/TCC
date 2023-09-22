def acima_da_media(lista):
    media = sum(lista) / len(lista)
    lista.insert(1,media)
    lista.sort()
    nota_de_corte = lista.index(media)
    return lista[nota_de_corte+1:]