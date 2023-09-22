def filtra_pares(tuplas4):
    filtragem = []
    filtragempar = []
    for i in range(len(tuplas4)):
        if tuplas4[i]%2 == 0:
            filtragem += [i]
        filtragempar = filtragem
        
    return filtragempar