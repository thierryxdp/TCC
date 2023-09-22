def qtd_divisores(n):
    '''função que conta o número de divisores que um número n possui;
    int->int'''
    qtd = 0
    divisores = [1,2,3,4,5,6,7,8,9,10]
    for elem in divisores:
        if n%elem==0:
            qtd += 1
        else:
            qtd = qtd
    return qtd