def soma_h(n):  
    '''Função que calcula o valor de H
    Recebe o número
    Retorna o valor de H'''
    H = 0
    for i in range(1,n+1):
        H = H + 1.0/i
    return round(H, 2)