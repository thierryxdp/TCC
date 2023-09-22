def uppCons(frase):
    return ''.join(caractere.upper() if caractere in 'bcdfghjklmnpqrstvxwyzç' else caractere for caractere in frase)