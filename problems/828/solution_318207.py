def primo (numero):
    multiplo = 0
    
    for c in range (2, numero):
        if c <= 2:
            primo = True
        else: 
            primo = False
         
    return primo