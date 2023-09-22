def conta_frases(texto):
    """ str -> int;
    Função que conta o número de frases que aparecem no texto."""
    l = texto.split('. 'and'...'and'!'and'?')
    o = texto.count('. 'and'...'and'!'and'?')
    r = 0 + (texto.count('. ') + texto.count('...') +
             texto.count('!') + texto.count('?'))
    if texto[-1] == '.':
        r = r + 1
    if '...' in texto:
        r = r - texto.count('...')
    return r