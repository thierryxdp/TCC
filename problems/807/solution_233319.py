def conta_frases(texto):
    """ str -> int;
    Função que conta o número de frases que aparecem no texto."""
    l = texto.split('. 'and'...'and'!'and'?')
    r = texto.count('. 'and'...'and'!'and'?')
    return r