def lingua_p(palavra):
    
    palavra_p = ''
    for letra in palavra:
        
        if letra in 'aeiou':
        	palavra_p += letra+'p'+letra
        else:
            palavra_p += letra
            
    return palavra_p