def acima_da_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    me = soma/quantidade
    list.sort(notas)
    return notas[m:]