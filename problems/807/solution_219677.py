def conta_frases(texto):
    '''conta o numero de frases presentes em um texto,
    onde as frases apenas terminam em '?','!','...' e '.';
    sring -> int'''
    return 0.5*(len(texto.split('.'))+len(texto.split('?'))+len(texto.split('!'))+len(texto.split('...')))