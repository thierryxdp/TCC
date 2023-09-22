def fatorial(n):
    '''Função que dado um número retorna o fatorial
    dele
    entrada=int
    saida=int'''
    h=n
    i=n
    while i>1:
        h=h*(i-1)
        i=i-1
    return h