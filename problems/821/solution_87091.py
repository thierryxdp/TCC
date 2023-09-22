def fatorial(n):
    '''Função que dado um numero n (int), calcula o fatorial dele'''
    cont = 1  
    n_fat = 1  

    while cont <= n:
        n_fat = n_fat * cont 
        cont = cont + 1
        
    return n_fat