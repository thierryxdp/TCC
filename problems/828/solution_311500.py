def primo(numero):
    
    divisores=[]
    
    
    for elemento in range(numero+1):
        
        if elemento !=0 and numero%elemento==0:
            list.append(divisores,elemento)
      
    if len(divisores)==2:
        return True
    else:
        return False