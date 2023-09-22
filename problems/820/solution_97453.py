def posLetra(frase, letra, n):
    q = 0
    lista = []

    for i in frase:
        if i == letra:
            q += 1
            lista.append(str.index(frase, i))

    if n > q:
        return -1

    else:
        lista.sort()
        return lista[range(lista)]