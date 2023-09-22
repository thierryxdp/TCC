def fatorial(n):
    '''dado um numero n, calcula o fatorial desse número'''
    produto = 1
    while n-1 != 0:
        produto = produto * n
        n = n - 1
    return produto

def faltante(lista):
    '''dada uma lista numarada de 1 a n, retorna o numero que está faltando
    lista -> int'''
    produtoNovo = 1
    lista = list.sort(lista)
    max(lista) = n
    while n-1 != 0:
        produtoNovo = produtoNovo * n
        n = n - 1
    return fatorial//produtoNovo