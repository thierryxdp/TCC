def acima_da_media(lista):
    media = sum(lista) / len(lista)
    nova_lista = list()
    for valor in lista:
        if valor > media:
            nova_lista.append(valor)
    nova_lista.sort()
    return nova_lista