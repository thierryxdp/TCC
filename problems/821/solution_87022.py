def fatorial(n):
    '''função que dado um número, retorna o fatorial deste. int -> int'''
    contador = n
    while (contador > 1):
        produto = n * (n - 1)
        contador = contador - 1
    return produto