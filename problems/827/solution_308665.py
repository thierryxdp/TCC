def qtd_divisores(num):
    """ Funçao que conte quantos divisores um numero tem"""
    num = int
    for divisores in range(1,num+1):
        if num % divisores == 0:
            return divisores