def fatorial(n):
    contador = n
    indice = n-1
    while contador > 1:
        contador *= indice
        indice -= 1
    return contador