def filtra_pares(a):
    retorno=a[0] or a[1] or a[2] or a[3]
    if a[0]%2==0:
        retorno=retorno,a[0]
    if a[1]%2==0:
        retorno=retorno,a[1]
    if a[2]%2==0:
        retorno=retorno,a[2]
    if a[3]%2==0:
        retorno=retorno,a[3]
        return retorno