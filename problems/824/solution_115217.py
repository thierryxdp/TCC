def uppCons(frase):
    '''
    funçao que recebe uma frase e retorna a frase com consoantes maiusculas
    str -> str
    '''
    frase_nova=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyzç':
            frase_nova=frase_nova=str.upper(frase[i])
        else:
            frase_nova=frase_nova+frase([i])
            i=i+1
    return frase_nova