def soma_h(N):
    '''função que calcula e retorna o valor H com N termos, em que N é
    o inteiro dado como entrada; int -> float'''
    H = 0
    for i in range(1,N+1):
        H = H + 1/i
    return round(H,2)