def qtd_divisores(n):
    '''conta quantos divisores um numero possui'''
    divisores = []
    
    for i in list(range(n)):
        if (n % i == 0):
            divisores.append(i)
    
    return len(divisores)