def soma_h(N):
    '''
    Funçao que recebe um numero e calcula a soma de
    todos os numeros ate n invertidos
    int->float
    '''
    H=0
    for i in range(0,N):
        H=H+(i**(-1))
       
    return round(H,2)