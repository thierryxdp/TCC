def primo (numero):
    
    for c in range (1, numero):
        if numero % c == 0:
            primo = False
        else: 
            primo = True
    return primo