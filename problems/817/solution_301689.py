def acima_da_media(list):
    s= list([n for n in list if n>=5])
    list.sort(s)
    return s