def primo (numero):
    
    for c in range (1, numero+1):
        if numero % c == 0 and numero % 1 == numero:
            primo = 1
        else:
            primo = 0 
    return primo