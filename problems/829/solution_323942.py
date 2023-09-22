def soma_h(N):
    '''
    função que calcula uma determinada soma com N termos
    representada por H. N é dado como parâmetro
    int -> float
    '''
    total = 0
    for num in range(1, N + 1):
        inverso = (1/num)
        total = total + inverso
        
    return round(total, 2)