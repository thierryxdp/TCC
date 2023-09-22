def soma_h(N):
    '''
    	A função recebe um número N e retorna o resultado da sequência de soma H
        para N termos com uma aproximação de 2 casas decimais. A soma H é dada por
        1/1+1/2+1/3+...+1/N.
        N -> int
        int -> float
    '''
    r = 0
    for i in range(1,N+1):
        r += 1/i
    r = round(r,2)
    return r