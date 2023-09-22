def acima_da_media(notas):
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.reverse(notas)
    return notas[:list.index(notas, n)]