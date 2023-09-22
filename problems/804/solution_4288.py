def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def filtra_pares (a, b, c, d):
    x = (a, b, c, d)
    return list(filter(par,x))