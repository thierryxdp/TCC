def soma_h(n):
    '''.'''
    soma = 1
    d = 2
    a = 1/d
    
    
    while d <= n:
        soma = soma + a
        d = d + 1
        a = 1/d
        
        
    
    return round(soma,2)