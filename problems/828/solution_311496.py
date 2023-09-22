def primo(numero):
    
    divisores=[]
    elemento=1
    
    for elemento in range(numero):
        
        if numero%elemento==0:
            list.append(divisores,elemento)
        elemento+=1
        return len(divisores)