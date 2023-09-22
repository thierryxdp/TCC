def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = math.floor(soma/qntd)
    a = media + 1
    if media in notas:
        return notas[a:]
    else:
        return