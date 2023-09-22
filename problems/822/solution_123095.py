def repetidos(lista):
    """ """
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return len(l)