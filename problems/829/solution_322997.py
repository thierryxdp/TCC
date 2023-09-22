def soma_h(n):
    '''função que retorna o valor de h com n termos, dado como parâmtero n, que é inteiro     como entrada
    int --> float'''
    H = 0
    for x in range(1,n+1):
        H = H + 1/x
    return round(H,2)