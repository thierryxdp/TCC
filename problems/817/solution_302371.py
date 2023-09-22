def acima_da_media(lista):
    x= [n for n in lista if n>(sum(lista))/(len(lista))]
    list.sort(x)
    return x