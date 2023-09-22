def soma_h(n):
    
    H = 1
    termos = range(2, n+1)
    
    for indice in termos:
        H += 1/indice
    
    H = round(H, 2)
    return H