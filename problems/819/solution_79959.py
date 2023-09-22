def filtraMultiplos(lista, div):
    multiplos = []
    i = 0
    if lista[i]%div:
        multiplos = multiplos + [lista[i],]
    i = i+1
    return multiplos