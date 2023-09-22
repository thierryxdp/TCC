def conta_frases(texto):
    '''Função que, dado um texto no formato de string, retorna o número de frases do texto; str -> int.'''
    a = str.split(texto, ".")
    b = str.split(texto, "!")
    c = str.split(texto, "?")
    d = str.split(texto,"...")
    return len(a) + len(b) + len(C) + len(d)