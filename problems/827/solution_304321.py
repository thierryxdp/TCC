def qtd_divisores(num):
    """Conta o número de divisores que um dado número tem
    int -> int"""
    divisores = 0
    for i in range(1, num+1):
        if num%i == 0:
            divisores += 1
    return divisores