def acima_da_media(notas,media):
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    indice = list.index(notas,media)
    return notas[indice+1:]