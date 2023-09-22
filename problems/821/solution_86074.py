def fatorial(n):
    '''Função que retorna o fatorial de um número n
    int -> int'''
    x=n-1
    multiplicacao=n
    while x>=1:
        multiplicacao*=x
        x-=1
    return multiplicacao