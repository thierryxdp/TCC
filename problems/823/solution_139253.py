def faltante(l):
    i = 1
    while i < len(sorted(l)):
        if l[i] != l[i - 1] + 1:
            return l[i - 1] + 1