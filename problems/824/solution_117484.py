def uppCons(frase):
    
    i = 0
    
    l_novafrase=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            l_novafrase += str.upper(frase[i])
        else:
            l_novafrase += frase[i]
            
        i += 1
        
    return l_novafrase