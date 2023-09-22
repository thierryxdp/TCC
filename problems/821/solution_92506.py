def fatorial(num):
    '''funcao que dado um numero retorna seu fatorial'''
    if num < 2:
        return 1
    else:
        return num * fatorial(num-1)