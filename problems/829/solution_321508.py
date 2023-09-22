def soma_h(N):
    H = 1
    
    for i in list(range(2, N+1)):
        H += i ** -1
        
    return H