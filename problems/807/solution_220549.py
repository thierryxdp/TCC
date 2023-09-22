def conta_frases(texto):
    ''' Conta o numero de frases presentes em um texto,
    onde as frases terminam apenas em '.','...','?' e '!';
    str->int'''
    return 0.5*(len(texto.split('.'))+len(texto.split('?'))+len(texto.split('!'))+len(texto.split('...')))