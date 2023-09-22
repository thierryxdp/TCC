def qtd_divisores(n):
    """ Funçao que conte e retorne quantos divisores um numero tem """
    
    divisores = []
    for i in range(1,n+1):
        if n%i==0:
            divisores.append(i)
    num = len(divisores)
    return num