#
#
#
#

def conta_frases(texto):
    texto=str.replace(texto,'...','.')
    texto = list(texto)
    numero_frases = list.count(texto,'.') + list.count(texto,'!') + list.count(texto,'?')
    return numero_frases