def qtd_divisores(n):
    
    '''Função que dá a quantidade de divisores de um número dado como entrada. int -> int'''
    
    q = 0
    
    for i in range(1,n + 1):
        if n%i == 0:
            q = q + 1
    
    return q