def faltante(n):
    
    i=0
    numero_fora=0
    inteiros=[1,2,3,4,5,6,7,8,9]
    
    while i<len(n):
        
        if n[i] not in inteiros:
            numero_fora=n[i]
            
        i+=1
    
    return numero_fora