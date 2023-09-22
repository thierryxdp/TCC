def faltante(n):
    list.sort(n)
    i = 0
    z = 0 
    if n[0] > 1:
        return 1
    else:
        while i < len(n):
            if n[i]+1 == n[i+1]:
                z = z + 1
            i = i + 1
    return z