def uppCons(frase):
    '''
       recebe uma frase e a retorna com todas as suas
       consoantes em maiusculas(e os demais caracteres
       permanecem como antes)
       str -> str 
    '''
    i = 0
    consoantes = 'bcdfgcçhjklmnpqrstvwxyz'
    while i<len(frase):
        if frase[i] in consoantes:
            frase = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase