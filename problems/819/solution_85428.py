def eh_mult(x,n):
    if x % n == 0:
        return True
    if x % n != 0:
        return False




def filtraMultiplos(ls,n):
    r = []
    for x in ls:
        if eh_mult(x,n):
            list.append(r,x)
    
    return r