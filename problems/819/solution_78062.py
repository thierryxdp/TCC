def filtraMultiplos(t,n):
    """ """
    
    multiplos = ()
    proximo = 0
    while proximo<len(t):
        t[proximo]%n ==0
        multiplos = multiplos + (t[proximo])
        return multiplos