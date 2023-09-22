def primo(numero):
    dvezes=0
    for n in range(2,numero+1): 
        if numero%n==0: 
            dvezes+=1 
    if dvezes==0: 
        return (True) 
    else:
        return (False)