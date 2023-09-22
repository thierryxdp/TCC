def soma_h(N):
    '''
    '''
    
    resultado = 0 
    for i in range(1, N+1):
        resultado = resultado + (1.0/i)

    resultado = round(resultado,2)
    return resultado