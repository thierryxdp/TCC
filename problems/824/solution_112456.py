def uppCons (frase):
    '''dada uma frase, retorna a frase com as consoantes em maiusculas
       : str -> str
    '''
    i = 0
    frase = frase.upper
    while i <len(frase):
        if frase[i] in 'AEIOUaeiou':
            frase[i].lower
    return frase