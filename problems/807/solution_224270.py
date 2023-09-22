#
#
#
#
def conta_frases(texto):
    texto.replace('...','.')
    texto = list(texto)
    numero_frases = list.count(texto,'.') + list.count(texto,'!') + list.count(texto,'?')
    return numero_frases