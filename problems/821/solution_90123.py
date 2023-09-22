def fatorial(n):
    '''funçao que calcula e retorna o fatorial de um numero n.int->int'''
   
    fatorial = 1
    proximo = 0
    while n>1:
        fatorial = fatorial  * n
        n = n - 1
    proximo = proximo + 1 
    return fatorial