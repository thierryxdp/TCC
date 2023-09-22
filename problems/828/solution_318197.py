def primo (numero):
    
    for c in range (1, numero+1):
        if c <= 2:
            primo = True
        if numero % c == 0:
            primo = False
    return primo