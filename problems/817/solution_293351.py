def acima_da_media(notas):
    n = sum(notas)//len(notas)
    notas[0:0] = [n]
    list.sort(notas)
    x = list.index(notas,n)
    return notas[x+1:]