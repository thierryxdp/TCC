def uppCons(frase):
    frasenova = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = frase.upper()
        else:
            frase[i] 
            frasenova+= frase[i]
        i+=1
    return frase