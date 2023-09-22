def soma_h(n):
    '''Retorna o valor H com N termos onde N é um número inteiro dado como entrada
    int -> float'''
    H = 0
    for i in range(1,n,-1):
        H += 1/i
    return round(H,2)