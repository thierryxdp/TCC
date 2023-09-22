def filtra_parees(tupla):
    pares=[]
    for i in tupla:
        if(i%2==0):
            pares.append(i)
    return tuple(pares)