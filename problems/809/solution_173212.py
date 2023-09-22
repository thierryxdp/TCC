def intercala(lista1,lista2):
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada