def conta_frases(s):
    '''
    Esta função recebe um texto e retorna um número (int) correspondente a quantas
    frases existem neste texto.
    
    Parametros
    ----------
    s (string) : texto
    '''
    c = 0
    l = ['.', '?', '!']
    s = s.replace('...', '.')
    for i in range(len(s)):
        if s[i] in l:
            c += 1
    return c