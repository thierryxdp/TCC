def acima_da_media (x):
    soma = sum(x)
    quantidade = len(x)
    media = soma // quantidade
    x.append(media)
    x.sort()
    return x[int(media) + 1:]