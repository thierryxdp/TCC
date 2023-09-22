def fatorial(a):
    '''
    	A função recebe um número a e retorna seu fatorial.
        a -> int
        int -> int
    '''
    i = 2
    f = 1
    while i <= a:
        f *= i
        i += 1
    return f