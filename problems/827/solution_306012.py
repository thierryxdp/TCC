def qtd_divisores(x):
    '''conta quantos divisores a entrada (x) tem. int,int->int'''
    y = 0
    for w in range (1, x+1):
        if x%w==0:
            y += 1
    return y