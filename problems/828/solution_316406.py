def primo(n):
    '''Dado um número inteiro n, retorna
    se ele é primo ou não.
    int -> bool'''
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    if(mult==0):
        t = True
    else:
        t = False
    return t