def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma//qntd
    a = media + 1
    if qntd == 1:
        return []
    if 0 in notas:
        a = soma//(qntd - 1)
        return notas[a:]