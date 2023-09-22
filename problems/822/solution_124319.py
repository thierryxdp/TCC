def repetidos(lista):
    q = 0

    for i in range(len(lista)):
        if i == lista[i]:
            q += 1

    return q