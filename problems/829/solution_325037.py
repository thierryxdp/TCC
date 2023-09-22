def soma_h(n):
    cont=0.0
    
    for x in range(1, n+1):
        cont+= 1/x
        return round(cont,2)