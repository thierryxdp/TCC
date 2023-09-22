def uppCons(frase):
    nova_frase=" "
    
    while(i<len(frase)):
        if (frase[i] not in "AEIOUaeiou"):
            list.append( nova_frase, str.upper(frase[i]))
        else:            
            list.append(nova_frase,frase[i])
       
        i=i+1
                        
    return str.join(" ",nova_frase)