def fatorial (n):
    '''função que dado um numero calcula o fatorial desse msm
    '''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat