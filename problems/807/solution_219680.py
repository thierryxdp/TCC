def conta_frases(texto):
    '''conta o numero de frases presentes em um texto,
    onde as frases apenas terminam em '?','!','...' e '.';
    string -> int'''
    num_frases=len(texto.split('.'))+len(texto.split('?'))+len(texto.split('!'))+len(texto.split('...'))