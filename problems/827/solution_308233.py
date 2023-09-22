def qtd_divisores(numero):
    
    i = 0
    
    for elem in range(1,numero+1):
        if numero%elem == 0:
            i = i+1
    
    return i