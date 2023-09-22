def uppCons(frase):
    s = ''
    for consoante in frase:
        if consoante in 'bcçdfghjklmnpqrstvxwyz':
            s += consoante.upper()
        else:
            s += consoante
    return s