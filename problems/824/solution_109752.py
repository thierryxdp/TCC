def uppCons(frase):
    frasenova = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = frase[i].upper()
            frasenova+= frase[i]
        i+=1
    return frase