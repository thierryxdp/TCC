def acima_da_media(lista):
    n_elementos = len(lista)
    media = sum(lista)/n_elementos
    maior = [n for n in lista if n > media]
    return sorted(maior)