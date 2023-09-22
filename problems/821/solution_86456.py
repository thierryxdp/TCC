def fatorial(n):
    '''funcao que calcula o fatorial de um numero recebido.int ->int'''
    fatorial = 1    
     while n>0:
        fatorial = n *(n-1) 
        n = n - 1        
        if n< 0:
            fatorial = 'indefinido'
            return fatorial