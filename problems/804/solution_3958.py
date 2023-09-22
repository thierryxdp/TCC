def filtra_pares(k):
    """Calcula e retorna uma nova tupla a partir de uma anterior, apenas com os valores pares da original na mesma ordem que se encontravam
    Entradas: tupla(k)
    tupla-->tupla"""
    tuplak2 = ()
    if k[0]%2==0:
        tuplak2=tuplak2+(k[0],)
    if k[1]%2==0:
        tuplak2=tuplak2+(k[1],)
    if k[2]%2==0:
        tuplak2=tuplak2+(k[2],)
    if k[3]%2==0:
        tuplak2=tuplak2+(k[3],)
        return tuplak2
    else:
        return tuplak2