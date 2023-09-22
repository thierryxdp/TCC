def repetidos(a):
    i=0
    
    repeticao=0
    while 1+i<len(a):     
        if a[i]==a[1+i]:        
            repeticao+= 1 
        i= i+1
    return repeticao