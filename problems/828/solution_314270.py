def primo(numero):
    
    
    
    lista=list(range(2,numero+1))    
    
    for e in lista:
        if numero%e == 0:
            return numero
             
        else:
            return False