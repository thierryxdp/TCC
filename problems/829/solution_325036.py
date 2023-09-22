def soma_h(N):
    cont=0.0
    
    for x in range(1, N+1):
        cont+= 1/x
        return round(cont,2)