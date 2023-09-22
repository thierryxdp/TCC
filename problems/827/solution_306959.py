def qtd_divisores(num):
    """retorna quantos divisores o numero de entrada tem
    int->int"""
    soma = 0
    for d in range(1,num+1):
        if num % d == 0:
            soma = soma + 1
    return soma