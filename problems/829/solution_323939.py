def soma_h(n):
    ''' 
    Funçao que recebe um numero inteiro e calcula o valor de H com n termos
    int -> float
    '''
    H = 0
    for i in range(1,n+1):
        H = H + (1/i)
    return round(H,2)