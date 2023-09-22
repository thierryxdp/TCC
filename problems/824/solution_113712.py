def teste(frase):
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
           frase= str(frase).upper()
        i=i+1
    return frase