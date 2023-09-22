def uppCons(frase):
    '''Torna as consoantes de uma frase maísculas'''
    i = 0
    novaFrase = ''
    while i < len(frase):
        if frase[i] not in 'aeiouãéíóú':
            novaFrase += frase[i].upper()
    
        else:
            novaFrase += frase[i].lower()
            
        i += 1

    return novaFrase