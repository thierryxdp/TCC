def fatorial(n):
    '''retorna o fatorial de n;
int->int'''

    i=1
    fatorial=1

    while i<=n:
        fatorial= fatorial*i
        i=i+1
    return fatorial