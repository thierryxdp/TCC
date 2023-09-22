def primo(numero):
    
    lista=list(range(1,numero+1))
    i=0    
    
    for e in lista:
        if numero == 2:
            return True
        if numero >2 and numero%2 !=0:
            return True
        if (numero%lista[i])!=0:
            return True