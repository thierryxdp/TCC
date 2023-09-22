def filtra_pares(a,b,c,d):
    x = [a,b,c,d]
    if a % 2 == 0:
        return True 
    if b % 2 == 0:
        return True 
    if c % 2 == 0:
        return True 
    if d % 2 == 0: 
        return True
    else:
        return False
list(filter(filtra_pares, x))