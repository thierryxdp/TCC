def maiores(lista, limite):
    list.insert(lista, 0, limite)
    list.sort(lista)
    posicao = list.index(lista, limite)
    return lista[posicao+1:]

def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return media, maiores(notas, media)