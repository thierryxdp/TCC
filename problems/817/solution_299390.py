def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.append(notas, media)
    list.sort(notas)
    list.reverse(notas)
    notas[:list.index(notas, media)]
    return notas