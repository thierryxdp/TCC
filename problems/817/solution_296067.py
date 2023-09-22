def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma//qntd
    if qntd == 1:
        return []
    if 0 and media in notas:
        list.remove(notas, 0)
        f = list.index(notas,media)
        return notas[f:]
    if 0 in notas and media not in notas:
        return notas[0:]
    if media in notas:
        c = list.index(notas, media)
        d = c + 1
        return notas[d:]
    if media not in notas:
        a = media + 1
        e = list.index(notas, a)
        f = e + 1
        return notas[e:]