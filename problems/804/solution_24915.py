def filtra_pares(valores):
    y = ()
    cont = 0
    for x in valores:
        if x%2 == 0:
            y[cont] = x
            cont = cont +1
            
    return y