def soma_h(n):
    '''.'''
    soma = 1
    d = n
    a = 1/d
    i = 0
    
    while i <= n:
        soma = soma + a
        d = d - 1
    i = i + 1
    
    return round(soma,2)