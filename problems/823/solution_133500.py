def faltante(l):
    i = 0
    r = 0
    while i < len(l) - 1:
        if l[i] == l[i+1] + 1:
            i = i + 1
            r = 0
        elif i == len(l) - 1:
            r = 0
        else:
            r = l[i] + 1
            i = i + 1
    return print(r)