def soma_h(N):
    H=0
    for i in range(N):
        H+=1/(i+1)
    return round(H,2)