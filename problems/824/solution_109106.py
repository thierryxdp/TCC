def uppCons(frase):
    i = 0
    novaFrase = ""
    while i < len(frase):
        if frase[i] in "qwrtypsdfghjklçzxccvbnm":
            novaFrase = novaFrase + str.upper(frase[i])
                 
        else:
            novaFrase = novaFrase + frase[i]
            
        i += 1
    
    return novaFrase