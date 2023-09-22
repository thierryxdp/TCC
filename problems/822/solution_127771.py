def repetidos(lista):
    list.sort(lista)
    i = 0
    while i < len(lista):
        if len(list[i]) != i:
            i += 1
    return len(list) - i