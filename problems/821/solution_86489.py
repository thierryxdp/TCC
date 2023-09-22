def fatorial(n,i):
    '''funcao que calcula o fatorial de um numero recebido.int ->int'''
    fatorial = 1 
    i=2
    while i <= n:
        fatorial = fat*i 
        i=i+1
    if n < 0:
        fatorial = 'indefinido'  
        return fatorial 
        return i