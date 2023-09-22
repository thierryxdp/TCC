def acima_da_media(notas):
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.sort(notas)
    if n in list.index(notas,s):
        return notas[list.index(notas, n)+1:]
    else:
        return notas[list.index(notas, n)+2:]