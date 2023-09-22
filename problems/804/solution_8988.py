def filtra_pares(tupla):
    
    pares=[]
    for i in range(tupla):
        if tupla[i]%2==0:
            pares.append(tupla[i])
    return pares