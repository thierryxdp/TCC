def filtra_pares(elemento1, elemento2, elemento3, elemento4):
    par1 = elemento1%2
    par2 = elemento2%2
    par3 = elemento3%2
    par4 = elemento4%2
    pares = ()
    if par1 == 0:
        pares = filtra_pares[1]
    if par2 == 0:
        pares = filtra_pares[2]
    if par3 == 0:
        pares = filtra_pares[3]
    if par4 == 0:
        pares = filtra_pares[4]