def fatorial(num):
    '''calcula o fatorial de número; int -> int'''
    i = 0
    acumulador = 1
    while (num - i) >= 1:
        acumulador = acumulador * (num - i)
        i = i + 1
    return acumulador