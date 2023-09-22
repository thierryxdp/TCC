def acima_da_media(notas):
    """ """
    a= notas +[5]
    list.sort(a)
    c=list.index(a,5)
    return a[c:]