def fatorial(num):
    ''' Essa função calcula o fatorial de um número
    int -> int'''
    i = 1
    fat = 1

    while i <= num:
        fat = fat * i
        i += 1
    return fat