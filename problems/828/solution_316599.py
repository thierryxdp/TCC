def primo(num):
    
    
    e_primo = True
    for div in range(2,int(num**1/2)+1):
        
        if not num%div:
            e_primo=False
            
    return e_primo