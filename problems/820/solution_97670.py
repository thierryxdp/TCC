def posLetra(t, l, n):
    correncias = []          
    for c in enumerate(t):           
        if c[1] == l:                
            correncias.append(c[0])  
    if n >= len(correncias):         
        return -1                    
    return correncias[n - 1]