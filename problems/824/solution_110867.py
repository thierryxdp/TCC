def uppCons(frase):
    
    i=0
    nova_frase=" "
    
    while(i<len(frase)):
        if (frase[i] not in "AEIOUaeiou"):
            nova_frase= nova_frase + str.upper(frase[i])
        else:            
            nova_frase= nova_frase,frase[i]
       
        i=i+1
                        
    return str(nova_frase)