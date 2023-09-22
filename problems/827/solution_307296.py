def qtd_divisores(num):
    """ """
    """ """
    divisores = 0
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    return divisores