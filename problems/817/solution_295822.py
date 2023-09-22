def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    a = list.index(lista, media)
    b = a+1
    return lista[b:]