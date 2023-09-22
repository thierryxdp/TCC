def uppCons(frase):
    '''
    funcao retorna a frase com as consoantes em letras maiusculas
    '''
    cons= ''
    for h in frase:
        if h in 'bcdfghçjklmnpqrstvxwyz':
            cons += h.upper()
        else:
            cons +=h
    return cons