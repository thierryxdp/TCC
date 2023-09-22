def soma_h(n):
    '''retorna o valor de H de acordo com  função dada
    int-->float'''
    h=0
    for i in [1,n+1]:
        h=h+(1/i)
    return round(h,2)