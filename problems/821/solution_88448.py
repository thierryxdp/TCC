def fatorial(n):
    """Dado um numero, calcula-se o fatorial dele. int>int"""
    i = 1
    res= 1
    while (i <= n):
        res*=i
        i+=1
    return res