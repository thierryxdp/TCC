def qtd_divisores(num):
    '''funcao que calcula quantos divisores um numero tem; int -> int'''
    indice = 0
    for indice in range(num):
        if num % indice == 0:
            return soma