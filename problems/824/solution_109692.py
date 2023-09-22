def uppCons(frase):
    s = ''
    caractere=0
    while caractere<len(frase):
        if caractere in s=='bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
    return s