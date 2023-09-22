def conta_frases(texto):
    '''conta o numero de frases presentes em um texto,
    onde as frases apenas terminam em '?','!','...' e '.';
    string -> int'''
    num_frases=len(texto.split('.'))+len(texto.split('?'))+len(texto.split('!'))+len(texto.split('...'))
    if '.' in texto:
        num_frases=num_frases-1
    if '...' in texto:
        num_frases=num_frases-1
    if '?' in texto:
        num_frases=num_frases-1
    if '!' in texto:
        num_frases=num_frases-1  
    return num_frases