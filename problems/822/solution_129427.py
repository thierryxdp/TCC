def repetidos(lista):
    r = []
    e = 1
    while e <= len(lista):
        a = lista[e]
        b = lista[e+1]
        if a == b:
            r.append(lista[e])
            e = e + 1
        elif a != b:
            r.append('x')
            e = e + 1
        return r