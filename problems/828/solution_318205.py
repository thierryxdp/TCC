def primo (numero):
    for c in range (1, numero+1):
        if not numero % c == 0:
            primo = False
        if numero % c == 0:
            primo = True
        
    return primo