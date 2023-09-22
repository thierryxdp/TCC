def fatorial(n):
    contador = n
    while contador > 1:
        contador *= contador-1
        contador -= 1
    return contador