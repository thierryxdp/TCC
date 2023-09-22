def acima_da_media(notas):
    n=sum(notas)/len(notas)
    list.append(notas,n)
    list.sort(notas)
    x=list.index(notas,n)
    list.remove(notas,float(n))
    return notas[x:]