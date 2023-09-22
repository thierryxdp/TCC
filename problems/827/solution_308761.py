def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    if n==0 or n<0:
        return 0
    qtd=0
    for num in n:
        if num%n == 0:
            qtd = count.qtd
            return qtd