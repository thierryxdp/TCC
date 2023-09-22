def fatorial(n):
    '''Função que recebe um int(n);
e retorna o fatorial deste int.
int->float'''
    f = 1
    i = 1
    while i <= n:
        f = f*i
        i = i+1
    return f