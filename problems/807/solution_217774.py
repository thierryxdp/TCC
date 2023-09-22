def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto. string -> int"""
    return str.count(texto,'?') + str.count(texto, '!') + str.count(texto,'.') - 2*str.count(frase, '...')