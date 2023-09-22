def qtd_divisores(n):
    '''.'''
    d = 1 
    qtd = 0
    while d < n:
        if n%d == 0:
            qtd = qtd + 1
            d = d + 1
            
    return qtd