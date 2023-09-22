def qtd_divisores(n):
    """ Funçao que conte quantos divisores um numero tem"""
    
    for i in range(1,n//2):
        if (n % i) == 0:
            return i