def qtd_divisores(n):
    """ Funçao que conte quantos divisores um numero tem """
    if n==0 or n<0:
        return 0
    divisores = 0
    divisores=list(range(1,n+1))
    for i in divisores:
        if n%i == n:
            divisores = list.count(divisores,i)
            return divisores