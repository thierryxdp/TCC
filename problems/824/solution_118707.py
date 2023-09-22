def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    s = ''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s += str.upper(frase[i]) # transforma em maiúscula
        #else: # não é consoante minúscula, mantém como no original
        i=i+1    #s += caractere
    return s