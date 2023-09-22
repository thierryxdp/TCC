def filtra_pares (a):
    return tuple(filtra(a))
def el1(a):
    if a[0]%2 == 0:
        return a[0]
    else:   
        return None
def el2(a):
    if a[1]%2 == 0:
        return a[1]
    else:
        return None    
def el3(a):
    if a[2]%2 == 0:
        return a[2]
    else:
        return None
def el4(a):
    if a[3]%2 == 0:
        return a[3]
    else:
        return None 
def filtra(a):
    return str(el1), str(el2), str(el3), str(el4)