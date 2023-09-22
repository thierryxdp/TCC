def fatorial(n):
    contador = n
    while contador > 2 :
        n *= contador - 1
        contador -= 1
    return contador