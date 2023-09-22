def filtra_pares(valores):
    filtro=[]
    for x in valores:
        if x%2==0:
            filtro +=[x]
    return tuple(filtro)