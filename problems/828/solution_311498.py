def primo(numero):
    
    divisores=[]
    
    
    for elemento in range(numero):
        
        if elemento !=0 and numero%elemento==0:
            list.append(divisores,elemento)
      
    return len(divisores)