def f(n):
    contador = n
    if n ==1 or n==0:
        return 1
    while contador > 1:
        n = n*(contador - 1)
        contador -= 1
    return n