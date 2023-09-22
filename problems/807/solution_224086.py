#
#
#
#
def conta_frases(texto):
    texto=list(texto)
    n=list.count(texto,'.')+list.count(texto,'!')+list.count(texto,'?')+list.count(texto,"...")
    return n