def primo(n):
    '''Dado um valor n, diga se ele é primo ou não; int -> bool'''
    mult=0
    for numero in range (2,n):
        if n%numero!=0:
            return mult
        else:
            mult=mult+1
            return mult
    if mult==0:
        return True
    else:
        return False