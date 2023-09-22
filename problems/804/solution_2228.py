def filtra_pares(a):
    retorno=a
    if a[0]%2==0:
        retorno = a[0]
    if a[1]%2==0:
        retorno=retorno and a[1]
    if a[2]%2==0:
        retorno=retorno and a[2]
    if a[3]%2==0:
        retorno=retorno and a[3]