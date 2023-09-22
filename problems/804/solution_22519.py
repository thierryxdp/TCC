def filtra_pares (tuplas):
    """retorna apenas os elementos pares de uma tupla na ordem em que se encontram."""
    pares=()
    if (tuplas[0]%2)==0:
    	pares+=(tuplas[0],)
    if (tuplas[1]%2==0):
        pares+=(tuplas[1],)
    if (tuplas[2]%2==0):
        pares+=(tuplas[2],)
    if (tuplas[3]%2==0):
        pares+=(tuplas[3],)
    return pares