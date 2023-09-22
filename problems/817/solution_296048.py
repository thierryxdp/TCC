def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma//qntd
    if qntd == 1:
        return []
    if 0 in notas:
        b = soma//(qntd - 1)
        return notas[b:]
    if media in notas:
        c = list.index(notas, media)
        return notas[c:]