#
#
#
#
def conta_frases(texto):
    texto=list(texto)
    n=list.count(texto,'.')+list.count(texto,'!')+list.count(texto,'?')+list.count(texto,'...')
    o=list.find(texto,'...')
    return n+o