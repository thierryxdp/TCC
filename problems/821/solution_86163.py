def fatorial(x):
    '''Retorna o fatorial de x;
    int -> int'''
    n = list(range(1,x+1))
    i = 0
    f = 1
    while i < len(n):
        
        f = n[i]*f
        i = i+1
    return f