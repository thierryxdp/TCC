def soma_h(N):
    ''' Funcao calcula a soma dos termos da serie: 
    H = 1 + 1/2 + 1/3 + ... + 1/N 
    ate o termo N, dado como entrada;
        
    int -> float '''
        
    H = 0
        
    for termo in range(1,N+1):

        H = H + 1/termo
            
    return H