def primo(n):
    '''
    	essa função detecta se o número é primo ou não retornando em valor booleano
        int -> bool
    '''
    i = 0
    for x in range(1, n):
        if n % x == 0:
            i = i +1
    if i > 1:
        return False
    else:
        return True