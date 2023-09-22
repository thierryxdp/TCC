def acima_da_media(notas):
    x=sum(notas)/len(notas)
    list.append(notas,x)
    list.sort(notas)
    list.reverse(notas)
    r = notas[0:list.index(notas,x)]
    list.sort(r)
    if len(notas)==1:
        return []
    else:
        return r