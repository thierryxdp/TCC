def conta_frases(s):
    """Função que conta o número de frases que aparecem em um texto.
    str->int"""
    return str.count(s,'.') + str.count(s,'!')+ str.count(s,'?') + str.count(s,'...') - 3*(str.count(s,'...'))