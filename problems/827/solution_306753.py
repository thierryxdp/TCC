def qtd_divisores(numero): 
    ndd=0
    for n in range(1,numero): 
        if numero%n==0: 
            ndd=ndd+1 
    return ndd