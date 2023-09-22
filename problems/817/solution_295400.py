def acima_da_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma/quantidade
    list.sort(notas)
    return notas[media:]