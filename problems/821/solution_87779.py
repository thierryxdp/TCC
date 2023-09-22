def fatorial(n):
    """a funcao recebe um numero (n) e se esse numero for maior ou igual
a 2 que é o minimo fatorial ele fatora o numero e dá o seu retorno"""
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat