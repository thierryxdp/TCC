def piltra_pares (tupla):
    guarda_pares = []
    for i in tupla:
        if i % 2 == 0:
            guarda_pares.append(i)
    return tuple(guarda_pares)