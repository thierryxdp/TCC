def repetidos(lista):
    s = []
    r = []
    i = 1
    while i < len(lista):
        if lista[i] == lista[i-1]:
            r.append('x')
        elif lista[i] != lista[i-1]:
            s.append('x')
        i += 1
    return len(r)