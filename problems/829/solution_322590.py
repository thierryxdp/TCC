def soma_h(num):
    '''Função que retorne o valor de soma_h
    float -> float'''
    h = 0
    for x in range(1,num+1):
        h += 1/x
    return round(h,2)