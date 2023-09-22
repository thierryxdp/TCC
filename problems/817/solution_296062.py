def acima_da_media(notas):
    list.remove(notas, 0)
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma//qntd
    if qntd == 1:
        return []
    if media in notas:
        c = list.index(notas, media)
        d = c + 1
        return notas[d:]
    if media not in notas:
        a = media + 1
        e = list.index(notas, a)
        f = e + 1
        return notas[e:]