def filtra_pares(x):
    m=()
    if x[0]%2==0:
       m+=(x[0],)
    if x[1]%2==0:
        m+=(x[1],)
    if x[2]%2==0:
        m+=(x[2],)
    if x[3]%2==0:
        m+=(x[3],)
    return m