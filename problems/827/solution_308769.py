def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    if n==0 or n<0:
        return 0
    n = []
    for num in list(range(1,n+1)):
        if num%n == 0:
            qtd = list.count(n,num%n)
            return qtd