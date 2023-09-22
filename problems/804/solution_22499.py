def filtra_pares (tup):
    """retorna apenas os elemtneos pares de uma tupla na ordem em que se encontram.
    tuple->>tuple"""
    if (tup[0]%2)==0):
        pares+=(tup[1],)
    if (tup[1]%2)==0):
        pares+=(tup[1],)
    if (tup[2]%2)==0):
        pares+=(tup[2],)
    if (tup[3]%2)==0):
        pares+=(tup[3],)
    return pares