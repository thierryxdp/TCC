def posLetra(s,l,n):
    ocorrencias = []                 
    for i in enumerate(s):           
        if i[1] == l:                
            ocorrencias.append(i[0])  
    if n >= len(ocorrencias):        
        return -1                    
    return ocorrencias[n - 1]