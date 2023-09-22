def fatorial(n):
    """Calcula o fatorial do número n
    int->int"""
    c=1
    f=1
    while c<=n:
        f=f*c
        c+=1
    return f