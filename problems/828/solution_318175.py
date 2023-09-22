def primo (numero):
    
    for c in range (1, numero+1):
        if numero >= 2:
            primo = False
        if numero < c:
            primo = True
    return primo