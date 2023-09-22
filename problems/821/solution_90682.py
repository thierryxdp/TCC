def fatorial(num):
    '''calcula o fatorial de um numero, dado esse numero de entrada.
    num - > int
    return -> int'''
    
    m = 1
    i = 1


    while i < num:
        if i < num:

            m = m * (i+1)

        i+= 1
    return m