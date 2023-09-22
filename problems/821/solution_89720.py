def fatorial(numero):
    '''função que calcula o fatorial de um número,numero, desejado'''
    i = 0
    fat = 1
    numero2 = numero
    while i < numero:
        fat = fat * numero2
        numero2 = numero2 - 1
        i = i + 1
    return fat