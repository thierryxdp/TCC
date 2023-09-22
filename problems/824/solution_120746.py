def uppCons(frase):
    return ''.join(caractere.upper() if caractere in 'bcdfghjklmnpqrstvxwyz' else caractere for caractere in frase)