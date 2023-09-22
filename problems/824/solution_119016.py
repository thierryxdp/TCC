def uppCons(frase):
    novaFrase = ""
    i = 0
    
    while i < len(frase):
        if frase[i] in ('a', 'e', 'i', 'o', 'u'):
            novaFrase += frase[i]
        else:
            novaFrase += frase[i].upper()
        
        i += 1
    
    return novaFrase