def filtraMultiplos (t, N):
    multiplos = ()
    proximo = 0
    while proximo <len(t):
        if t[proximo]%N == int:
            multiplos = multiplos + (t[proximo],)
        proximo = proximo + 1

    return multiplos