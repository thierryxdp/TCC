def filtra_pares(tupla):
    filt = ()
    if tupla[0]%2 ==0:
        filt = filt+(tupla[0],)
    if tupla[1]%2 ==0:
        filt = filt+(tupla[1],)
    if tupla[2]%2 ==0:
        filt = filt+(tupla[2],)
    if tupla[3]%2==0:
        filt = filt+(tupla[3],)
    return filt