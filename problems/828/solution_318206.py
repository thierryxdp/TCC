def primo (numero):
    multiplo = 0
    
    for c in range (2, numero):
        if numero % c == 0:
            primo = True
            multiplo += 1      
        else: 
            primo = False
         
    return primo