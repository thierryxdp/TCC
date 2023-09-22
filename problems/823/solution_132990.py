def faltante(lista):
    i = 1
    while i < len(lista):
        l = list.sort(lista)
        n = l[i]
        if n - 1 != l[i - 1]:
            r = r + (l[i] - 1)
            i = i + 1
        i = i + 1
    return r