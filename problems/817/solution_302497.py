def acima_da_media (x):
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade
    lista.append(media)
    lista.sort()
    return x[media + 1:]