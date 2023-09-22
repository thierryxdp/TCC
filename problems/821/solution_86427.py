def fatorial(numero):
    """Essa função retorna o fatorial do numero inserido na função"""
    """int->int"""
    f=1
    c=1
    while c<=numero:
        f=f*c
        c=c+1
    return f