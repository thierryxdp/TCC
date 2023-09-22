def soma_h(n):
    '''função que calcula e retorna o valor H com N termos
    int->float'''
    
    h = 0
    den = 0
    
    for i in range(n):
        num = 1
        den = den + 1
        h += (num/den)
        
    return round(h,2)