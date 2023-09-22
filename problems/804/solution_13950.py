def filtra_pares ((1,2,3,4)):
    x = [1,2,3,4]
    if 1 % 2 == 0:
        return True 
    if 2 % 2 == 0:
        return True 
    if 3 % 2 == 0:
        return True 
    if 4 % 2 == 0: 
        return True
    else:
        return False
list(filter(filtra_pares, x))