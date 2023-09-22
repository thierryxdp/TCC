def acima_da_media(list):
    s=[n for n in list if n>=5]
    list.sort(s)
    return s