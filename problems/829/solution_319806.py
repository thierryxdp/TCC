def soma_h(N):
    '''Calcula e retorna o valor H da "Soma H", com N termos onde N é inteiro e dado como entrada
    int -> float'''
    H = 1
    for i in range(N):
        if i>0:
            H = H + 1/i
    return round(H, 2)