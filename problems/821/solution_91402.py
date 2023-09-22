def fatorial (n):
    '''essa funçao calcula o fatorial de um numero n
int -> int'''
    fato =1
    i=2
    while i <n:
        fato=fato*i
        i=i+1
    return fato