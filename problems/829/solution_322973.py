def soma_h(n):
    '''Função que calcula e retorna o valor de H com n termos, onde n é inteiro e é dado como entrada:
    int -> float'''
    H = 1
    i = 2
    while i <= n:
        H = H + 1/i
        i = i + 1
    return round(H,2)