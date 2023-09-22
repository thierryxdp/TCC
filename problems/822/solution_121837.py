def repetidos(l):
    contador = 0
    i = 0
    while i < len(l):
        if l[i] == l[i+1]:
            contador = contador + 1
        i = i +1
    return contador