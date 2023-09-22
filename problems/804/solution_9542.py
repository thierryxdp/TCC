def filtra_pares(notas):
    m= notas[0]
    p= notas[1]
    c= notas[2]
    e= notas[3]
    numero=()
    if (%(m)/2==0):
        numero =numero+str(m)
    if (%p/2==0):
        numero = numero+str(p)
    if (%c/2==0):
        numero = numero+str(c)
    if (%e/2==0):
        numero = numero+str(e)
        return numero