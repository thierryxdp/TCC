def qtd_divisores(n):
    '''
    	A função recebe um número e calcula a quantidade de divisores que esse número
        tem.
        n -> int
        int -> int
    '''
    a = range(1,n+1)
    r = 0
    for i in n:
        if n % i == 0:
            r += 1
    return r