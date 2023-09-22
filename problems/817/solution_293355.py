def acima_da_media(notas):
    n = sum(notas)/len(notas)
    notas[0:0] = [n]
    list.sort(notas)
    x = list.index(notas,n)
    z = x+1 
    if x == z:
        return notas[x+2:]
    else:
        return notas[z:]