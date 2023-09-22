def filtra_pares(a):
    retorno=a[0] and a[1] and a[2] and a[2] and a[3]
    if a[0]%2==0:
        retorno=retorno,a[0]
    if a[1]%2==0:
        retorno=retorno,a[1]
    if a[2]%2==0:
        retorno=retorno,a[2]
    if a[3]%2==0:
        retorno=retorno,a[3]
    return retorno