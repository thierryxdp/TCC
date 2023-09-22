def fatorial(n):
    """função retorna o resultado da fatorial do número dado. INT->INT"""
    i=1
    result=1
    while i<=n:
        result=result*i
        i=i+1
    return result