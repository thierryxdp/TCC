def qtd_divisores (num):
    '''conta quantos divisores tem o numero'''
    for i in range( num//2+1):
        if num % i == 0:
            return i
    return num