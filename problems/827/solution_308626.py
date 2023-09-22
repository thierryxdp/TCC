def qtd_divisores(n):
    '''
    	A função recebe um número e calcula a quantidade de divisores que esse número
        tem.
        n -> int
        int -> int
    '''
    a = range(n+1)
    a.remove(0)
    r = 0
    for i in a:
        if a % i == 0:
            r += 1
    return r