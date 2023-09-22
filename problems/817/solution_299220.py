def acima_da_media(notas):
    notas2 = notas[:]
    media = sum(notas)/len(notas)
    list.insert(notas, 0, media)
    list.sort(notas)
    if list.count(notas, media)==1:
        notas[list.index(notas, media)+1:]
        return notas