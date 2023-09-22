def fatorial(n):
    """Para fatorar um numero, digite:
    int->int"""
    
    while n>1:
        n-=1
        fatorial =fatorial * n
        return fatorial