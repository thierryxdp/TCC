def soma_h (n):
    '''realiza a soma de 1+1/2+...+1/n , sendo n um
    inteiro
    int -> float'''
    
    h = 0
    if n != 0:
        for i in range(1,n+1):
            h += 1/i
        return round(h,2)
            
    else:
        return 'infinito'