def primo(num):
    '''Retorna true, se o número de entrada for primo,
       ou false, caso contrário;
       int -> bool'''
    for n in range(2,num):
        if num%n==0:
            return False
    return True