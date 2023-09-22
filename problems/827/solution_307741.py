def qtd_divisores(num):
    """retorna a quantidade de divisores de um numero
    int -> int"""
    divisores = 0
    for numero in range(1,num+1):
        if num % numero == 0:
            divisores += 1
    return divisores