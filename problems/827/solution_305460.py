def qtd_divisores(n):
    """ Dado um número n, retorna a quantidade de divisores desse número.
    int -> int
    """
    count = 0
    for i in range(1, n + 1):
        if(not n % i):
            count += 1
    return count