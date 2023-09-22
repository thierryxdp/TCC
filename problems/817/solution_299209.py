def acima_da_media(notas):
    notas2 = notas[:]
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.sort(notas)
    list.reverse(notas)
    return notas