def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    a = list.index(notas,media)
    return notas[a+1:]