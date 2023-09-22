def uppCons(frase):
    '''
    
    '''
    x = 0 
    while x < len(frase):
        if frase[x] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvxXyYWwXxZzçÇ':
            frase = frase.replace(frase[x],frase[x].upper())
            x += 1
            return frase