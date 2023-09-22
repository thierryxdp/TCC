def acima_da_media(notas):
    n = sum(notas)/len(notas)
    notas[0:0] = [n]
    list.sort(notas)
    x = list.index(notas,n)
    if x == n and notas :
        return notas[x+2:]
    else:
        return notas[x+1:]