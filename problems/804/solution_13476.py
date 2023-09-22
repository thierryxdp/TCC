# Função que filtra os números pares de uma tupla
def filtra_pares(a):
    
    if a[0] % 2 == 0:
        valor0 = a[0]
        n0 = (valor0,)
    else:
        valor0 = ()
        n0 = (valor0)
    if a[1] % 2 == 0:
        valor1 = a[1]
        n1 = (valor1,)
    else:
        valor1 = ()
        n1 = (valor1)
    if a[2] % 2 == 0:
        valor2 = a[2]
        n2 = (valor2,)
    else:
        valor2 = ()
        n2 = (valor2)
    if a[3] % 2 == 0:
        valor3 = a[3]
        n3 = (valor3,)
    else:
        valor3 = ()
        n3 = (valor3)
    return n0+n1+n2+n3