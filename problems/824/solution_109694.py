def uppCons(frase):
    return ''.join(caractere.upper() if caractere in 'bcçdfghjklmnpqrstvxwyz' else caractere for caractere in frase)