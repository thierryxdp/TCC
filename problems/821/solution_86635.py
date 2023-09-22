def fatorial(x):
    '''retorna o fatorial de um número x;
    int -> int'''
    multp = 1
    soma = 1
    y = x+1
    while multp < y:
        soma = soma*multp
        multp = multp + 1
    return soma