def soma_h(n):
    termos = 0    
    for termo in range(1,n+1):
        x = 1/termo
        termos += x
    return(round(termos,2))