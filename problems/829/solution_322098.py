def soma_h(N):
    
    '''Função que calcula a soma dos inversos dos números inteiros até o número de entrada N. int -> int'''
    
    H = 0
    
    for i in range(1,N + 1):
        H = H + (1/i)
    
    return round(H,2)