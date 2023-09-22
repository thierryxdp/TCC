def primo(n):
    '''Dado um valor n, diga se ele é primo ou não; int -> bool'''
    mult=0
    for numero in range (1,n):
        if n%numero==0:
            mult=mult+1
    if mult>1:
        return False
    else:
        return True