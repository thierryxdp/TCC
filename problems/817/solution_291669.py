def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    indice = list.index(notas,media)
    lista = notas[indice+1:]
    list.remove(lista,media)
    return lista