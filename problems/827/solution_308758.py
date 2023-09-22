def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    for divisores in n:
        if n%n == 0:
            return divisores