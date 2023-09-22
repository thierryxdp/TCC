#tuple-->tuple
def filtra_pares(tupla):
#função que retorna os elementos pares de uma tupla proveniente da tupla de entrada
    tuplaX = ()
    if tupla[0] % 2 == 0:
        tuplaX = tuplaX + (tupla[0],)
    if tupla[1] % 2 == 0:
        tuplaX = tuplaX + (tupla[1],)
    if tupla[2] % 2 == 0:
        tuplaX = tuplaX + (tupla[2],)
    if tupla[3] % 2 == 0:
        tuplaX = tuplaX + (tupla[3],)
    return tuplaX