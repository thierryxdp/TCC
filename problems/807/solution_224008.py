#
#
#
#
def conta_frases(texto):
    n=list.count(texto,'.')+list.count(texto,'!')+list.count(texto,'?')+list.count(texto,'...')
    return n