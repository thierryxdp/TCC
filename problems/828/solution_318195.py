def primo (numero):
    
    for c in range (1, numero+1):
        if numero % c == 0:
            primo = True
        else: 
            primo = False
    return primo