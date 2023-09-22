def maiores(x, y):
    lista = []
    for i in x:
        a = i+y
        if a > y:
            lista += [i]
    return lista