def acima_da_media(notas):
    n=sum(notas)/2
    list.append(notas,n)
    list.sort(notas)
    x=list.index(notas,n)
    return notas[x+1:]