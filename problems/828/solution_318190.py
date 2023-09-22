def primo (numero):
    
    for c in range (1, numero+1):
        if numero % c == 0:
            primo = False
        if numero <= 2: 
            primo = True
        else: 
            primo = True
    return primo