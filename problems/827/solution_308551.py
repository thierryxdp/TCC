def qtd_divisores(num):
    '''Retorna quantos divisores um número tem, dado esse número de entrada.
    num -> int
    return -> int'''
    divisores = 0
    i = 1
    
    for i in range(1, num + 1):
        
        if num % i == 0:
            divisores += 1
            
    return divisores