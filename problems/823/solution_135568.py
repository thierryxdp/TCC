def faltante(n):
    list.sort(n)
    i = 0
    ind = ()
    while (n[i] + 1) == n[i+1]:
        i = i + 1
    return i