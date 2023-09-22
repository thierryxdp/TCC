#
#
#
#
def conta_frases(texto):
    texto=list(texto)
    n=list.count(texto,'.')+list.count(texto,'!')+list.count(texto,'?')+list.count(texto,'.'*3)
    return n