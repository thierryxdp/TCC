def filtra_pares(a):
    tupla = ()
    if a[0]%2 == 0:
        tupla = a[0]
    elif a[1]%2 == 0:
        tupla = tupla + a[1]
    elif a[2]%2 == 0:
        tupla = tupla + a[2]
    elif a[3]%2 == 0: 
        tupla = tupla + a[3]
    return tupla