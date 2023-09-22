def fatorial(n):
    '''calcula e retorna o fatorial de um numero n'''
    x = n
    c = 1
    resultado = 1
    while c <= x:
        resultado = resultado*c
        c = c + 1
    return resultado