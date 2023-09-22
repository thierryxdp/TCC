def uppCons(frase):
    
    nova_frase = ''
    i = 0
    
    while i < len(frase):
        
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            maiuscula = str.upper(frase[i])
            nova_frase += maiuscula
            i += 1
            
        else:
            nova_frase += frase[i]
            i += 1
            
    return nova_frase