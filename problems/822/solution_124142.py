def repetidos(lista):
    q = 0

    for i in lista[0:len(lista) - 1]:
        a = lista[lista.index(i) + 1]

        if i == a:
            q += 1

    return q