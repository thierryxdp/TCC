def primo (numero):
    
    for c in range (2, numero):
        if numero % c == 0:
            primo =  False
            break
        else: 
            primo = True
        
         
    return primo