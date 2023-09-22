def uppCons(frase):
    return ''.join(l.lower() if l in 'AEIOU' else l for letter in frase)