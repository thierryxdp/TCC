def soma_h(x):
    '''A função retorna a soma nos 1/N ternos (x)
    int -> float'''
    
    h = []
    
    for numero in range(1,x+1):
        a = 1/numero
        
        list.append(h,a)
        
    b = sum(h,2)
    return round(b,2)