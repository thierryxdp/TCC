def fatorial(n: int) ->int:
    '''Recebe um número e retorna o fatorial desse numero.'''
    i = 0
    fat = 1
    while i < n:
        fat = fat*i
    	i = i+1
    return fat