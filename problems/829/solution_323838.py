def soma_h(N):
    '''
    Funçao que recebe um numero e calcula a soma de
    todos os numeros ate n invertidos
    int->float
    '''
    H=0
    for i in range(N):
        H=H+(N**(-1))
    return H