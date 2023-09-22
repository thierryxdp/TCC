#esta funça reaçiza a filtragem de números pares
#int-> int
def filtra_pares(d):
    np=()
    if d[0]%2==0:
        np+=(d[0],)
    if d[1]%2==0:
        np+=(d[1],)
    if d[2]%2==0:
        np+=(d[2],)
    if d[3]%2==0:
        np+=(d[3],)
    return np