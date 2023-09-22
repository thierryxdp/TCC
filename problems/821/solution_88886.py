def fatorial(n):
    contador = n
    indice = n-1
    while indice > 1:
        contador *= indice
        indice -= 1
    return contador