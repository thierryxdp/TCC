def uppCons(frase):
    '''
    
    '''
    x = 0 
    while x < len(frase):
        if frase[x] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvyYWwXxZzçÇ':
            frase = frase.replace(frase[x],frase[x].upper())
            x += 1
            return frase