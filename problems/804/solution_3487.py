def filtra_pares(t):
    Tpar = "("
    for n in t:
        if n%2 == 0:
            Tpar = str(Tpar) + str(n)
    Tpar = str(Tpar) + ")"
    return print(Tpar)#Start your python function here