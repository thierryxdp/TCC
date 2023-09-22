def qtd_divisores(num):
    """ Funcao que recebe um numero inteiro "num" de entrada,
    e retorna a quantidade total de divisores que esse numero 
    possui """
    """ int -> int"""
    divisor = 0
    for a in range(1, num + 1):
        if num % a == 0:
            divisor += 1
    return divisor
    #Casos de teste:
    """ qtd_divisores(40)
    >>> 8
        qtd_divisores(15)
    >>> 4
        qtd_divisores(892)
    >>> 6 """