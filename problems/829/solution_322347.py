def soma_h(N):
    '''funcao que recebe um numero inteiro positivo N que representa o numero de termos da soma como dado de entrada e retorna o valor da soma H
    int -> float'''
    H=0
    for i in range(1,N+1):
        H=H+(1/i)
    return round(H,2)