def faltante(l):
    i = 0
    if len(l) == 1:
        if l[0] == 1:
            return 2
        else:
            return l[0] - 1
    while i < len(sorted(l)):
        if l[i] != l[i - 1] + 1:
            return l[i - 1] + 1
        i += 1
    return sorted(l)[len(l) - 1] + 1