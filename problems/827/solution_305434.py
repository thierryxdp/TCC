def qtd_divisores(numero:int)->int:
    """ A função conta quantos divisores um número tem, e retorna a quantidade de divisores deste número"""
    soma = 0
    for num in range(1,numero+1):
        if numero % 2 == 0:
            soma += 1