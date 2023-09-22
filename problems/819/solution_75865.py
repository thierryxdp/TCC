def filtraMultiplos (l, n):
    multiplos = []
    contador = 0
    while contador < len(l):
        if l[contador]%n == 0:
            multiplos = multiplos + [l[contador],]
        contador += 1
    return multiplos