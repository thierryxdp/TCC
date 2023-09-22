#Start your python function here
def filtra_pares(tup):
    """..."""
    NovaT = ()
    if tup[0]%2 == 0:
        NovaT = NovaT + (tup[0],)
    if tup[1]%3 == 0:
        NovaT = NovaT + (tup[1],)
    if tup[2]%2 == 0:
        NovaT = NovaT + (tup[2],)
    if tup[3]%2== 0:
        NovaT = NovaT + (tup[3],)
    return NovaT