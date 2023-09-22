def filtra_pares(t):
    """ A função filtra os pares de uma lista e retorna em uma tupla
    os numeros pares
    list --> tuple"""
    r=()
    if t[0]%2==0:
        r=r+(t[0],)
	if t[1]%2==0:
        r=r+(t[1],)
    if t[2]%2==0:
        r=r+(t[2],)
    if t[3]%2==0:
        r=r+(t[3],)
    return r