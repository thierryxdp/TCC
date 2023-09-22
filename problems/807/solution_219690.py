def conta_frases(texto):
    '''conta quantas frases existem em um texto, onde 
    as frases podem terminar apenas com '.','...','?' e '!';
    string -> int
    '''
    
    if '.' in texto:
        num_frases=len(texto.split('.'))-1-len(texto.split('...'))-1
    if '...' in texto:
        num_frases=num_frases+len(texto.split('...'))-1
    if '?' in texto:
        num_frases=num_frases+len(texto.split('?'))-1
    if '!' in texto:
        num_frases=num_frases+len(texto.split('!'))-1
    return num_frases