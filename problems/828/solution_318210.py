def primo (numero):
    
    for contador in range (2, numero):
        if numero % contador == 0:
            primo =  False
            break
        else: 
            primo = True
        
         
    return primo