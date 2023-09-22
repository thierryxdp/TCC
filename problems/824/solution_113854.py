def uppCons(frase):
    '''funcao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas
       : str -> str
    '''
    i = 0
    fraseM = ''
    while i < len(frase):
        if frase(i) not in 'AEIOUaeiou':
            fraseM = fraseM + frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase