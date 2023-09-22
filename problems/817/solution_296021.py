def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    qntd = len(notas)
    media = soma/qntd
    return notas[media:]