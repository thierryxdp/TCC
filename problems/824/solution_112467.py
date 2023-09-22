def uppCons (frase):
    '''dada uma frase, retorna a frase com as consoantes em maiusculas
       : str -> str
    '''
    i = 0
    frase = ''
    while i <len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i].upper
        i=i+1
    return frase