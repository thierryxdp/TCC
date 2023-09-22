def qtd_divisores(num):
    """Essa função serve para calcular quantos divisores um número tem
    int->int"""
    divisores = 0
    for numeros in range(1,num+1):
        if num%numeros == 0:
            divisores += 1
    return divisores

#qtd_divisores(67) == 2
#qtd_divisores(12) == 6
#qtd_divisores(13) == 2