def fatorial(n):
    """funcao que retorna o fatorial dado numero n;
    int -> int"""

    i = n
    f = 1

    while i > 0:

      f = f * i

      i = i - 1 

    return f