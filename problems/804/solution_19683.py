def filtra_pares (x):
    def par (n):
        if n%2==0:
            return true
        else:
            return false
    return (filter(par,x))