def acima_da_media(notas):
    x=sum(notas)
    y=len(notas)
    h=x/y
    x=list.append(notas,h)
    y=list.index(notas,h)
    m=list.sort(notas)
    g=lista[y+1::1]
    return g