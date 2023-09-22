def faltante(n):
    list.sort(n)
    i = 0
    ind = ()
    z = 0
    while i < len(n):
        while n[z] == n[z+1]:
            z = z + 1
        i = i + 1   
    return z