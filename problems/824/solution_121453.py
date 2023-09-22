def uppCons(frase):
    minusculas = 'bcçdfghjklmnpqrstvxzwy'
    maiusculas = 'BCÇDFGHJKLMNPQRSTVXZWY'
    conversor = str.maketrans(minusculas, maiusculas)
    return frase.translate(conversor)