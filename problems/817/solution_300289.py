from math import ceil

def acima_da_media(notas):
    media = ceil(sum(notas)//len(notas))
    notas.append(media)
    lista = sorted(notas)
    media_indice = lista.index(media)
    
    if media not in lista:
        notas.append(media)
    return lista[media_indice + 1:]