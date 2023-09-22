#
#
#
#
def conta_frases(texto):
    str.split(texto)
    n=list.count(texto,'.')+list.count(texto,'!')+list.count(texto,'?')+list.count(texto,'...')
    return n