def fatorial(x):
    """função para calcular o fatorial de um determinado numero; inti-->int"""
    x=-1
    while x!=0:
        if x<=1:
            return 1
        else:
            return (x*(x-1))