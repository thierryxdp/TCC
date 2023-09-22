def faltante(n):
    
    i=0
    numero_fora=0
    inteiros=[1,99999]
    
    while i<len(n):
        
        if n[i] not in inteiros:
            numero_fora=n[i]
            
        i+=1
    
    return numero_fora