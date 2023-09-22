def soma_h(n):
    '''funcao que calcula o valor da soma e retorna o valor de H;
    int -> float'''
    H = 0
    for i in range(1,n + 1):
        H += 1// i
    return round(H,2)