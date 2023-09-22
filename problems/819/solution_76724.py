def filtraMultiplos(lista,num):
    i=0
    multiplos = []
    while i < len(lista):
        if lista[i]%num == 0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos