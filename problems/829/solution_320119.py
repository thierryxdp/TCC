def soma_h (n):
    ''' função que calcula o respectivo H para o número fornecido,
        onde H = 1 + 1/2 + 1/3 ... + 1/n
        [int--> float]'''
    H = 0

    for inteiro in range(1,n+1):
        H += 1/inteiro

    return round(H,2)