def acima_da_media(lista):
    media = sum(lista)/(1.0*len(lista))
    aprovados = maiores(1,media)
    return aprovados