def primo(numero):
    
    lista=list(range(1,numero+1))
    i=0    
    
    for e in lista:
        if (numero%lista[i-1])==0:
            return False
        if (numero/numero)==0:
            return True
            i+=1
    return True