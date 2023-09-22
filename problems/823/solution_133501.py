def faltante(l):
    i = 0
    r = 0
    if len(l) > 1:
        while i < len(l) - 1:
            if l[i] == l[i+1] + 1:
                i = i + 1
                r = 0
            elif i == len(l) - 1:
                r = 0
            else:
                r = l[i] + 1
                i = i + 1
    elif len(l) = 1:
        r = l[0] + 1
    return print(r)