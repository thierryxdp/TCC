def conta_frases(texto):
    ''' Conta o numero de frases presentes em um texto,
    onde as frases terminam apenas em '.','...','?' e '!';
    str->int'''
    return texto.count('.')+ texto.count('!')+ texto.count('?')-2*texto.count('...')