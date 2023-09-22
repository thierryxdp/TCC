def primo (numero):
    
    for c in range (1, numero+1):
        if numero % c == 0:
            primo += 1
        else:
            primo += 0 
    return primo