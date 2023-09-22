def fatorial(num):
    """função que dado um número, calcule o fatorial deste número.
    (Não usar a função factorial do módulo math).int -> complex"""
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat