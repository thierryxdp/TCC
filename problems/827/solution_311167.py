def qtd_divisores(n):
    ''' função que recebe um número como entrada 
    conte quantos divisores ele tem
    int, float --> int'''
    divisores = 0 
    for i in range (1, n+1): 
        if n % i == 0:
            divisores += 1
    return divisores