def filtra_pares(y):
    tupla=()
    if int(y[0])%2==0:
        tupla=tupla+(y[0],)
    if int(y[1])%2==0:
        tupla=tupla+(y[1],)
    if int(y[2])%2==0:
        tupla=tupla+(y[2],)
    if int(y[3])%2==0:
        tupla=tupla+(y[3],)
        return tupla