def fatorial(num):
    '''
    Função calcula o fatorial de um número
    int -> iint
    '''
    i = 1
    fat = 1

    while i <= num:
        fat = fat * i
        i += 1
    return fat