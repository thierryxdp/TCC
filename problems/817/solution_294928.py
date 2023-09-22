def acima_da_media(notas):
    """ """
    x = sum(notas)
    y = len(notas)
    z= (x/y)
    
    a= notas +[z]
    list.sort(a)
    c= list.index(a,z)
    return a[c+1:]