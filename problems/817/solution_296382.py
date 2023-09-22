def acima_da_media(notas):
    s = sum(notas)
    t = len(notas)
    m = (s/t)
    list.append(notas,m)
    list.sort(notas)
    a = list.index(notas,m)
    
    if notas[a]==notas[(a+1)]:
        return notas[(a+2):]
    
    if s==notas[a]:
        return []

    else:
        return notas[(a+1):]