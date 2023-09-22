# Primo

def primo(num):
    '''Dado um número, retorna se ele é primo ou não.
    int -> bool'''
    c = 0
    for x in range(2,num//2 + 1):
        if num%x == 0:
            c += 1
    if c == 0:
        return True
    else:
        return False