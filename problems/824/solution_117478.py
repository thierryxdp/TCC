def uppCons(frase):
    
    i = 0
    
    l_frase=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            l_frase += str.upper(frase[i])
        else:
            l_frase += frase[i]
            
        i += 1
        
        return l_frase