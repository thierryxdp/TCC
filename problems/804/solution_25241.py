def Par(n):
    return n%2==0

def filtra_pares(tup):
    'filtra os numeros pares de uma tupla com 4 valores tup->tup'
    tuppares=()
    if Par(tup[0]):
        tuppares = tuppares+(tup[0],)
    if Par(tup[1]):
        tuppares = tuppares+(tup[1],)
    if Par(tup[2]):
        tuppares = tuppares+(tup[2],)
    if Par(tup[3]):
        tuppares = tuppares+(tup[3],)
    return tuppares