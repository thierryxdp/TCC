def fatorial(n):
    """dado um numero, calula o fatorial dele"""
    num_final=1
    while n>1:
        num_final=num_final*n
        n=n-1
    return num_final