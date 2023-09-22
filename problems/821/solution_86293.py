def fatorial(n):
    ''' função que dado um número n qualquer de entrada retorna o fatorial desse número 
    int->int'''
    fatorial = 1
    while n>0:
        fatorial = fatorial*n
        n = n-1
    if n<0:
        fatorial = 'sem definição'
    return fatorial