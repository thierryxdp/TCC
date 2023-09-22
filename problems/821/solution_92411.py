def fatorial(num):
    '''Calcula o fatorial de um dado numero'''
    '''int->int'''
    if num<2:
        return 1
    else:
        return num*fatorial(num-1)