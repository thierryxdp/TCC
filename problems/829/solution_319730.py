def soma_h(N):
    '''funcao que dado um numero inteiro 
    'N' calcula o valor de H; int ->float'''
    
    H = 0
    for i in range(1,N+1):
        H = H + 1/i
    return round(H,2)