def soma_h(N):
    '''Função que retorna o valor de "H" com "N" termos de entrada: int -> float'''
    
    H = 0
    
    for indice in range(1, N+1):
        H += (1/indice)
    return round(H, 2)