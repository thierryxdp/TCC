def uppCons(frase):
    cons= ''
    for h in frase:
        if h in 'bcdfghçjklmnpqrstvxwyz':
            cons += caractere.upper()
        else:
            cons +=h
    return h