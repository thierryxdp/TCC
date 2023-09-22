def acima_da_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    m = soma/quantidade
    list.sort(notas)
    return notas[m:]