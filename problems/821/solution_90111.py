def fatorial(n):
    '''Esta e a funcao que dado um numero calcula o 
    fatorial deste numero'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat