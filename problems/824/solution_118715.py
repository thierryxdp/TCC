def uppCons(frase):
    '''
    Funçao que dado um frase, retorna a frase com somente as
    consoantes maiusculas
    str -> str
    '''
    s = ''
    i=0
    while i<len(frase):
        if frase[1] in frase:
            if frase[i] not in 'aeiouAEIOU':
                s += str.upper(frase[i]) # transforma em maiúscula
            else: # não é consoante minúscula, mantém como no original
                s += frase[i]
        i=i+1 
    return s