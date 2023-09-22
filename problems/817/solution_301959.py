def acima_da_media (lista):
    s = [n for n in lista if n > (list.sum(lista))/(len(lista))]
    return s