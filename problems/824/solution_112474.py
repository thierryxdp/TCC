def uppCons (frase):
    '''dada uma frase, retorna a frase com as consoantes em maiusculas
       : str -> str
    '''
    i = 0
    fraseM = ''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            fraseM = frase[i].upper
        i=i+1
    return fraseM