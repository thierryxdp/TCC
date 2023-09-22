def fatorial(n):
    '''
       Função que dado um numero calcula o seu fatorial
       int -> int
    '''

    num = 1
    fat = n

    while num < n:
        fat = fat * num
        num += 1
        
    return fat