def fatorial(n):
    '''calcula a fatorial do numero n'''
    '''int->int'''
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num