def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas
       : str -> str
    '''
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ'
    i = 0
    fraseM = ''
    while i < len(frase):
        if frase[i] in consoantes:
            frase = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase