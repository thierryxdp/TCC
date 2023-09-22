def posLetra(frase, l, n):
    qnt = []                  
    while  c in frase:           
        if c[1] == l:                
            qnt.append(c[0])  
        if n >= len(qnt):        
            return -1                    
    return qnt[n - 1]