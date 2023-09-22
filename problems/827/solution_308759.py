def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    if n==0 or n<0:
        return 0
    for i in list(range(1,n+1)):
        if n%i == 0:
            i=i+1
            return i