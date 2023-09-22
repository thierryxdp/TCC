def fatorial(num):
    '''Retorna o fatorial de num
    	int -> int'''
    i = 0
    fatorial = 1
    while i < num:
        fatorial = fatorial*num
        num = num-1
    i = i + 1
    return fatorial