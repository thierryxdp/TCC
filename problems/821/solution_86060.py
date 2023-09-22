def fatorial(num):
    """Para fatorar um numero, digite:
    int->int"""
    fatorial=num
    while num>1:
        fatorial*=num
        num-=1
        fatorial =fatorial * num
        return fatorial