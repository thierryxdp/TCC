def soma_h(N):
    '''
       funcao que retorna o valor H com N termos onde N é
       inteiro e dado como entrada
       int -> float 
    '''
    H = 0 
    for i in list(range(1,N+1)):
        H = H + (1/i)
    return round(H,2)