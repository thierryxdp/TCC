def qtd_divisores(numero:int)->int:
    """ A função conta quantos divisores um número tem, e retorna a quantidade de divisores deste número"""
    total_divisores = 0
    for num in list(range(1,numero+1)):
        if numero % 2 == 0:
            total_divisores += 1
        return total_divisores