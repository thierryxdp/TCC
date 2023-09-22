def fatorial(n):
    '''função que dado um número, retorna o fatorial deste. int -> int'''
    lista_fatorial = list(range(n + 1))
    pos = 1
    produto = 1
    while (pos < n + 1):
        produto = produto * lista_fatorial[pos]
        pos = pos + 1
    return produto