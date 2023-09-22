def conta_frases(texto):
    """ Funcao que conta o numero de frases que aparecem no texto
    str-->int"""
substr = '.','!','?','...'
return texto.count(substr)