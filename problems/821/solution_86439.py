def fatorial(n):
    '''funcao que calcula o fatorialde um numero recebido.int ->int'''
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n 
       n = n - 1
    if n< 0:
         fatorial = 'indefinido'
    return fatorial