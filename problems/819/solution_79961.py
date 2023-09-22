def filtraMultiplos(lista, div):
    multiplos = []
    i = 0
    while i<len(lista):
        if lista[i]%div==0:
        multiplos = multiplos + [lista[i],]
    i = i+1
    return multiplos