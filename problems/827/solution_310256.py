def primo(numero):
    soma=0
    for x in range(1,(numero+1)): 
        if numero%x==0:
            soma+=1 
    if soma==2: 
        return True 
    else: 
        return False