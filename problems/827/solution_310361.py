def qtd_divisores(n):
    '''.'''
    d = 1 
    qtd = 0
    for d in range(n>0):
  		d = 1
        if n%d == 0:
            qtd = qtd + 1
            d = d + 1
    return qtd