def filtra_pares(t):
    Tpar = ""
    for n in t:
        if n%2 == 0:
            Tpar = str(Tpar) + str(n)
    tpar = int(Tpar)
    return print(tpar)