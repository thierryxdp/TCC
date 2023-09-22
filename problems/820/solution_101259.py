def posLetra(frase, letra , n):
                      
    i=0
    while  i < len(frase):           
        if frase[i] == letra:                
            qnt =  str.index(frase,letra,n)  
        if n > qnt:        
            return -1                    
    i=i+1
    return qnt