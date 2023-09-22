def qtd_divisores(n):
    """função que retorna a quantidade de divisores do número n
    int -> int"""
    divisor = 1
    divisores = []
    while n >= divisor:
        if n % divisor == 0:
            divisores.append(divisor)
        divisor += 1
    return len(divisores)