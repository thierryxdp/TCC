def qtd_divisores(n):
    """dado um numero n inteiro, função retorna a quantidade de divisores que
    esse numero possui. int -> int"""
    divisores = 0
    divisor = []
    for c in range (1, n + 1):
        if n%c == 0:
            list.append(divisor, n/c)
            divisores = len(divisor)
            
    return divisores