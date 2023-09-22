def acima_da_media(notas):
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.sort(notas)
    if n in notas:
        return notas[list.index(notas, n):]
    elif n not in notas:
        return notas[list.index(notas, n)+2:]