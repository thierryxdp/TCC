def uppCons(texto):
    
    l = 0
    frase=''
    while l<len(texto):
        
        if texto[l]  not in 'abcdefjhijklmnopqrstuvwxyzç':
            
            frase+=texto[l]
  
        if texto[l] in 'abcdefjhijklmnopqrstuvwxyzç':
            
            frase+=str.upper(texto[l])
    
    	l+=1
    return frase