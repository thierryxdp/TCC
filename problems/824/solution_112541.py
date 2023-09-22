def uppCons(frase):
    cons= ''
    for h in frase:
        if h in 'bcdfghçjklmnpqrstvxwyz':
            cons += h.upper()
        else:
            cons +=h
    return cons