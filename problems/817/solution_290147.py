def acima_da_media(lista):
    soma = sum(lista)
    media = (soma)/(len(lista))
    list.append(lista,media)
    list.sort(lista)
    return list.pop(lista,media)