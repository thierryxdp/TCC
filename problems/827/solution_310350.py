def qtd_divisores(n):
    '''.'''
    d = 0
    qtd = 0
    for d in range(n):
        if n%d == 0 and 0 not in range(n):
            qtd = qtd + 1
    return qtd