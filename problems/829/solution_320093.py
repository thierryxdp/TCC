def soma_h(n):
    '''função que calcula e retorna o valor H com n termos'''
    '''int-->float'''
    h=0
    for i in range(1,n+1):
        h=h+1/i
    return round(h,2)