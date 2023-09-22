def fatorial(n):
    '''Função que calcula o fatorial de um número n
       int->int'''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fatorial(n-1)*n