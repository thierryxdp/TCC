def fatorial(n):
    contador = n
    k = 1
    if n == 0:
        return 1
    if n < 0 :
        return 'nao tem kkk'
    while contador > 2 :
        contador *= k
        contador -= 1
    return k