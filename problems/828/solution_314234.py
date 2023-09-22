def primo(numero):
    
    lista=list(range(1,numero+1))
    i=0    
    
    for e in lista:
        
        if (lista[i]%numero)!=0:
            return True