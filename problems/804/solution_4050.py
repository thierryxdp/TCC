def filtra_pares(k):
    """Funçao que retorna uma nova tupla contendo apenas os elementos pares da tupla
    original, na mesma ordem em que se encontravam"""
    tuplakp = ()
    if k[0]%2==0:
        tuplakp=tuplakp+(k[0],)
    if k[1]%2==0:
        tuplakp=tuplakp+(k[1],)
    if k[2]%2==0:
        tuplakp=tuplakp+(k[2],)
    if k[3]%2==0:
        tuplakp=tuplakp+(k[3],)
        return tuplakp
    else:
        return tuplakp