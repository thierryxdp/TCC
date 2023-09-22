def primo(n):
    '''
    	A função recebe um número inteiro e retorna True se esse for primo e False
        se esse for False.
        n -> int
        int -> bool
    '''
    a = range(2,n+1)
    for i in a:
        if n % i == 0:
            return False
    return True