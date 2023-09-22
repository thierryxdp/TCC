def acima_da_media(notas):
    s = sum(notas)
    t = len(notas)
    m = (s/t)
    list.append(notas,m)
    list.sort(notas)
    a = list.index(notas,m)
    return lista[(a+1):]