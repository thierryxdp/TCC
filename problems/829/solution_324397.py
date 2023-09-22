def soma_h (N):
    cont = 0.0
    for i in range (1, N+1):
        cont+= 1/i
        return round(cont, 2)