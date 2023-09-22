def soma_h(N):
    '''função que calcula e retorna, a partir de um número inteiro N, a soma H, definida por 1+1/2+...+1/N; int -> float'''
    
    H = 0
    for i in range(1, N+1):
        H =+ 1/i
    return H