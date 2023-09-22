def fatorial(num):
    '''funcao que dado um numero, calcule o fatorial deste numero.
    (Nao usar a funcao factorial do modulo math).
    int -> complex'''
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat