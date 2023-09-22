def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    if n==0 or n<0:
        return 0
    divisores = []
    for numero in n:
        if numero%n == 0:
            list.count(divisores,n)
            return divisores