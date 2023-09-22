def filtraMultiplos(l,n):
    ''''''
    divisiveis = ()
    x = 0
    while x < len(l):
        if l[x]%n == 0:
            divisiveis = divisiveis + (l[x])
        x = x + 1
    return divisiveis