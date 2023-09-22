def posLetra(frase, letra , n):
    qnt = 0                  
    i=0
    while  i < len(frase):           
        if frase[i] == letra:                
            qnt = qnt + str.index(frase,letra,n)  
        if n > len(qnt):        
            return -1                    
    i=i+1
    return qnt