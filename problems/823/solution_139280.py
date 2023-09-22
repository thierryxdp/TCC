def faltante(l):
    if 1 not in l:
        return 1
    i = 1
    while i < len(sorted(l)):
        if l[i] != l[i - 1] + 1:
            return l[i - 1] + 1
        i += 1
    return max(l) + 1