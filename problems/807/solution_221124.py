def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    numero_frases = str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'... ') + str.count(texto,'.')
    return numero_frases