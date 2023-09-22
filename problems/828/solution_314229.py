def primo(numero):
    
    lista=list(range(1,numero+1))
    i=0    
    
    for e in lista:
        if (numero%lista[i-numero+1])==0:
            i+=1
    return False