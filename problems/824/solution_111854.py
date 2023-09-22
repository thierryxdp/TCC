def uppCons(frase):
    frase_l = list(frase)
    
    for i in range(len(frase_l)):
        if frase_l[i] not in 'aeiouãõáéíóúàèìòùâêîôû ':
            frase_l[i] = str.upper(frase_l[i])
    
    return str.join('',frase_l)