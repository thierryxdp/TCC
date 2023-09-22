def uppCons(frase):
    '''Retorna a frase dada com suas consoantes em maiúsculas;
    str -> str'''
    i = 0
    upp_f = ''
    while i < len(frase):
        if frase[i] not in 'aeiou´~^':
            upp_f = upp_f + str.upper(frase[i])
            
        else:
            upp_f = upp_f + frase[i]
            
        i = i+1
        
    return upp_f