def qtd_divisores(x):
    '''
    função que calcula a quantidade de divisores que um numero "x" tem.
    int->int
    '''
    total=0
    for num in range(1,(x+1)):
        if x % num == 0 and numero > 0:
            total = total + 1
            
    return total