def acima_da_media(notas):
    n=sum(notas)/len(notas)
    list.append(notas,n)
    list.sort(notas)
    x=list.index(notas,n)
    list.remove(notas,n)
    if n in notas==True:
             return notas[x+2:]
    else:
        return notas[x:]