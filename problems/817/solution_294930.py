def acima_da_media(notas):
    """ """
    x = sum(notas)
    y = len(notas)
    z= int(x/y)

    if z in notas:
        a= notas
        list.sort(a)
        c= list.index(a,z)
        return a[c+1:]
    else: a= notas +[z]
    list.sort(a)
    c= list.index(a,z)
    return a[c+1:]