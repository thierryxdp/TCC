def filtraMultiplos(m,n):
    multiplos = list(filter(lambda x:x % n, m))
    return list(filter(lambda x: (x % n == 0), multiplos))