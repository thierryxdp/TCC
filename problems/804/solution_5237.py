#Start your python function here
def filtra_pares(tuplas4):
    filtragem = []
    for i in range(len(tuplas4)):
        if tuplas4[i]%2 == 0:
            filtragem = filtragem,tuplas4[i]
    return filtragem