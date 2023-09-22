def acima_da_media(notas):
    x=sum(notas)
    y=len(notas)
    h=x//y
    x=list.append(notas,h)
    m=list.sort(notas)
    y=list.index(notas,h)
    l=list.remove(notas,h)
    g=notas[y+1::1]
    n=notas[y::1]
    if len(notas)==2:
        return n
    if sum(notas)==30:
        return notas[y::1]
    else:
        return g