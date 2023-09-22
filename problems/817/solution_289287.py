def maiores_n(lista, n):
    list.append(lista, n)
    list.sort(lista, reverse=True)
    idx = list.index(lista, n)
    return lista[:idx]
def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.sort(notas, reverse=True)
    lista_maiores = maiores_n(notas, media)
    return media, lista_maiores