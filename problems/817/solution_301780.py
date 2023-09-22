def acima_da_media(lista):
    s=[n for n in lista if:
       n>(sum(lista))/(len(lista))]
    list.sort(s)
    return s