def qtd_divisores(num):
    '''funcao que calcula quantos divisores um numero tem; int -> int'''
    qtd = 0
    indice = 1
    while indice <= num:
        if num % indice == 0:
        qtd = qtd + 1
    return qtd