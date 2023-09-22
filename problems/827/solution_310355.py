def qtd_divisores(n):
    '''.'''
    d = 0
    a = n and a>0
    qtd = 0
    for d in range(a):
        if n%d == 0:
            qtd = qtd + 1
    return qtd