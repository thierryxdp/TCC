def filtra_pares(tupla):
    tupla = (a,b,c,d)
    resultado = ()
    if int(tupla[0])%2 == 0:
        resultado = resultado + (a,)
    if int(tupla[1])%2 == 0:
        resultado = resultado + (b,)
    if int(tupla[2])%2 == 0:
        resultado = resultado + (c,)
    if int(tupla[3])%2 == 0:
        resultado = resultado + (d,)
    return resultado