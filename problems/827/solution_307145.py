def qtd_divisores(num):
    '''funcao que calcula quantos divisores um numero tem; int -> int'''
    indice = 0
    for indice in range(1, num/2):
        if num % indice == 0:
            return indice