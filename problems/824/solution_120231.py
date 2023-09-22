def uppCons(frase):
    '''
    Recebe uma frase-string
    Retorna uma string contendo consoantes em maíusculo
    '''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        else: 
            s += caractere
    return s