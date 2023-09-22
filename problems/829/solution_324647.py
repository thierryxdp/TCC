def soma_h(N):
    H=[1]
    for numero in range(2,N+1):
        H.append((numero)**-1)
    somatorio=sum(H)
    return round(somatorio,2)