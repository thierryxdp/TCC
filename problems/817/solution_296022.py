def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma/qntd
    a = math.ceil(media)
    return notas[a:]