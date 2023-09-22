def faltante(l):
    i = 0
    while i < len(l):
        if l[i] != l[i+1] - 1:
            r = l[i] + 1
        return r