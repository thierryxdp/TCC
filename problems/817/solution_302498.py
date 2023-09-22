def acima_da_media (x):
    soma = sum(x)
    quantidade = len(x)
    media = soma / quantidade
    lista.append(media)
    lista.sort()
    return x[media + 1:]