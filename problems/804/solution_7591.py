def filtra_pares(a):
    """funcao que retorne os elemtos pares da tupla inical"""
    p=()
    m=()
    n=()
    q=()
    if a[0]%2==0:
        p=(a[0],)
    if a[1]%2==0:
        m=(a[1],)
    if a[2]%2==0:
        n=(a[2],)
    if a[3]%2==0:
        q=(a[3],)
    return p+m+n+q