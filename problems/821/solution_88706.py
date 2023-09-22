def fatorial(n):
    """funcao que recebe um numero e calcula o fatorial dele
    int -> int"""
    resultado=1
    i=1
    while i<=n:
        result=result*i
        i=i+1
    return result