def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    pontos = '.','!','?','...'
    if '.' in texto:
        pontos
    if '!' in texto:
        pontos
    if '?' in texto:
        pontos
    if '...' in texto:
        pontos
        return len(str.split(pontos))