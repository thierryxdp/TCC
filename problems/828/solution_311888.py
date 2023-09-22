def primo(n):
    '''Dado um valor n, diga se ele é primo ou não; int -> bool'''
    for numero in range (2,n):
        if n%numero!=0:
            return True
        else:
            return False