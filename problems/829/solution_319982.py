def soma_h(n):
    '''Calcula e retorna o valor de H, que é a soma de frações com denominadores de 1 a n'''
    '''int->float'''
    h=0
    for x in range(1,n+1):
        h=h+1/x
    return round(h,2)