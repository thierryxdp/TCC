def repetidos(lista):
    list.sort(lista)
    i = 0
    while i < len(lista):
        if i == i:
            i += 1
        else:
            i += 2
    return len(lista) - i