def faltante(L):
    i = 0
    j = 0
    n = len(L) + 1
    l = []
    while i <= n:
        l = l + [1*i]
        i = i + 1
    while j < n:
        if l[j] not in L:
            return l[j]
       	j = j + 1