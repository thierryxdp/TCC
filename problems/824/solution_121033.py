def uppCons(frase):
    tamanho = len(frase)
    frase2 = ''
    cont1 = 0
    
    while cont1 < tamanho:
        if frase[cont1] in 'bcdfghjklmnpqrstvwxyzç':
            frase2 = frase2 + str.upper(frase[cont1])
        else:
            frase2 = frase2 + frase[cont1]
        cont1 = cont1 + 1
        
    return frase2