def soma_h(n):
    cont = 0.0
    
    for i in range(1, n+1):
        cont+= 1/i
    return round(cont,2)