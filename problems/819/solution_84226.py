def filtraMultiplos([x], n):
    multiplos = []
    y = 0
    while y<len(x):
        if x[y]%n==0:
            multiplos = multiplos + (x[y],)
        y = y + 1
    return multiplos