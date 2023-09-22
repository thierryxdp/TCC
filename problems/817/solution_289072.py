def acima_da_media(lista):
    '''funcao que calcula a media de uma lista de notas e retorna uma lista com as notas acima dessa media
    lista->lista'''
    media = sum(lista)/len(lista)
    lista = lista+[media]
    list.sort(lista)
    index = list.index(lista, media) + list.count (lista, media)
    notas_acima_media: lista[index:]
    return notas_acima_media