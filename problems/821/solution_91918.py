def fatorial(n):
    contador = n
    k = 1
    if n == 0:
        return 1
    if n < 0 :
        return 'nao tem kkk'
    while contador > 2 :
        contador *= contador - 1
        contador -= 1
    return contador