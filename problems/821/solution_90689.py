def fatorial(num):
    '''
       Função que recebe um número calcula o fatorial deste número. 
       i:int.
       mult:int.
       num:int.
       return:int
    '''
    i = 1
    mult = 1
    while i <= num:
        mult = i*mult
        i += 1
    return mult