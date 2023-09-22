def soma_h(n):
    '''Dado um número, a função retorna o valor d H com n termos
       onde n é inteiro e dado como entrada
       int -> float
       Parametros:
       n: numero a ser digitado'''
    H = 0
    for c in range(1, n + 1):
        H += 1 / c
    return round(H, 2)