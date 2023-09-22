def fatorial(n):
    """função que dado um numero recebido, calcule o fatorial deste numero. int->int"""
    num=1
    while n >= 1:
        num=num*n
        n=n-1
    return num