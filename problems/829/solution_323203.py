def soma_h(N):
    "função que retorna o valor de H com N termos"
    "int -> float"
    
    H=[1]
    for numero in range(2, N+1):
        H.append((numero)**-1)
    sigma=sum(H)
    return round(sigma, 2)