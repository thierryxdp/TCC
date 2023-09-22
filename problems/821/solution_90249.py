def fatorial(n):
    """funcao que recebe um numero n e calcula o seu valor fatorial.
    int -> int"""
    if n<2:
        return 1
    else:
        return n*fatorial(n-1)