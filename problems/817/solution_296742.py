def acima_da_media(notas):
    x=sum(notas)
    y=len(notas)
    h=x/y
    x=list.append(notas,h)
    m=list.sort(notas)
    y=list.index(notas,h)
    g=notas[y::1]
    return g