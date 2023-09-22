def fatorial(num):
    '''calcula o fatorial de um numero, dado esse numero de entrada.
    num - > int
    return -> int'''
    fatorial = 0
    i = 1
    
    while i <= num:
        fatorial += (i * (i+1))
    
    i+= 1
    
    return fatorial