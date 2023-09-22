def soma_h(N):
    '''
        recebe um numero intero e retorna a soma das fracoes cujo dividendo e 1,
        os quocientes sao, a partir de N a sequenciq N, N-1, N-1,...,1
        entrada: inteiro
        saida: float
    '''
    sequencia = range(2, N+1)
    H = 1
    for chq in sequencia:
        H = H + chq ** -1
    return round(H, 2)