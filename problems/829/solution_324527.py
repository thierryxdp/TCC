def soma_h(n):
    H=1
    for numeros in range(2,n+1):
        H+=1/numeros
    return round(H,2)